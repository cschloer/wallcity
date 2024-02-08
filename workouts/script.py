import os
import pytz
from string import punctuation
import calendar
import json
import discord
from datetime import datetime, timedelta, date

API_TOKEN = os.environ.get("API_TOKEN")
workouts_channel_id = 1068205157516582912

stop_words = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "did",
    "do",
    "have",
    "for",
    "I",
    "if",
    "in",
    "into",
    "is",
    "it",
    "my",
    "no",
    "not",
    "of",
    "on",
    "or",
    "so",
    "such",
    "that",
    "the",
    "their",
    "then",
    "there",
    "these",
    "they",
    "this",
    "und",
    "to",
    "was",
    "will",
    "and",
    "with",
}

# since = datetime.today() - timedelta(days=30 * 6)
since = datetime(2023, 10, 2)


intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    try:
        today = datetime.utcnow().replace(tzinfo=pytz.utc)
        results = {
            "updated": str(today - timedelta(days=1)),
            "since": str(since),
        }

        # Get all user name and nick names into a dict
        user_names = {}
        ch = client.get_channel(workouts_channel_id)
        guild = ch.guild
        async for member in guild.fetch_members():
            user_names[member.id] = member.nick or member.display_name

        user_posts = {}
        user_posts_monthly = []
        posts_by_months = {}
        timestamps = []
        dates = []
        week_dates = []
        user_reactions_count = {}
        day_of_week_posts = {}
        total_emojis = 0
        popular_emojis = {}
        words = {}

        week_cutoff = today.replace(
            hour=0, minute=0, second=0, microsecond=0
        ) - timedelta(days=today.weekday())
        print(today)

        async for m in ch.history(
            after=since,
            before=today.replace(hour=0, minute=0, second=0, microsecond=0),
            limit=None,
        ):
            if len(m.attachments):
                user = m.author
                user_id = user.id
                if user_id not in user_posts:
                    user_posts[user_id] = []

                # Add users to
                user_posts[user_id].append(m)
                timestamp = calendar.timegm(m.created_at.utctimetuple())
                timestamps.append(timestamp)

                # Add dates
                current_day = m.created_at.date()
                if not len(dates) or dates[-1][0] != str(current_day):
                    dates.append([str(current_day), 0])
                dates[-1][1] += 1

                # Add week dates (smooth curve)
                if m.created_at < week_cutoff:
                    current_middle_week_date = (
                        m.created_at + timedelta(days=3 - m.created_at.weekday())
                    ).date()
                    if not len(week_dates) or week_dates[-1][0] != str(
                        current_middle_week_date
                    ):
                        week_dates.append([str(current_middle_week_date), 0])
                    week_dates[-1][1] += 1

                # Add user weekly
                current_month = m.created_at.strftime("%B")
                if (
                    not len(user_posts_monthly)
                    or user_posts_monthly[-1]["month"] != current_month
                ):
                    user_posts_monthly.append({"month": current_month, "users": {}})
                if user_id not in user_posts_monthly[-1]["users"]:
                    user_posts_monthly[-1]["users"][user_id] = 0
                user_posts_monthly[-1]["users"][user_id] += 1

                # Add day of week calculation
                weekday = m.created_at.weekday()
                if weekday not in day_of_week_posts:
                    day_of_week_posts[weekday] = 0
                day_of_week_posts[weekday] += 1

                # Add message content to word bubble
                for word in m.content.split(" "):
                    if not word.startswith("<@"):
                        word = word.strip(punctuation)
                        if word:
                            ratio = sum(map(str.isupper, word)) / len(word)
                            if ratio < 0.5:
                                word = word.lower()

                            if word not in stop_words:
                                if word not in words:
                                    words[word] = 0
                                words[word] += 1

                for reaction in m.reactions:
                    emoji = reaction.emoji
                    # Handle the repeat one emoji as a way to be part of a workout
                    if emoji == "🔂" and m.created_at.year >= 2024:
                        async for user in reaction.users():
                            if user.id != user_id:
                                # Increase everything
                                week_dates[-1][1] += 1
                                dates[-1][1] += 1
                                if user.id not in user_posts_monthly[-1]["users"]:
                                    user_posts_monthly[-1]["users"][user.id] = 0
                                user_posts_monthly[-1]["users"][user.id] += 1

                                day_of_week_posts[weekday] += 1
                                if user.id not in user_posts:
                                    user_posts[user.id] = []
                                user_posts[user.id].append(m)
                                timestamps.append(timestamp)

                    emoji_id = emoji if isinstance(emoji, str) else emoji.id
                    if emoji_id not in popular_emojis:
                        popular_emojis[emoji_id] = {
                            "count": 0,
                            "emoji": emoji if isinstance(emoji, str) else emoji.url,
                            "is_url": not isinstance(emoji, str),
                        }
                    popular_emojis[emoji_id]["count"] += reaction.count
                    total_emojis += reaction.count
                    # Commented out for now because it takes too long
                    """
                    async for user in reaction.users():
                        if user.id not in user_reactions_count:
                            user_reactions_count[user.id] = 0
                        user_reactions_count[user.id] += 1
                    """

        """
        if not len(user_posts_monthly) or user_posts_monthly[-1][
            "month"
        ] != week_cutoff.strftime("%B"):
            user_posts_monthly.append(
                {"month": week_cutoff.strftime("%B"), "users": {}}
            )
        """
        # Add words
        results["words"] = [[w, words[w]] for w in words.keys() if words[w] > 3]

        # Add timestamps
        results["timestamps"] = timestamps
        results["dates"] = dates
        results["week_dates"] = week_dates

        # Sort emojis
        sorted_emojis = sorted(
            [v for v in popular_emojis.values()],
            key=lambda t: t["count"],
            reverse=True,
        )

        # Add day of week days
        sorted_day_of_week_number = sorted(
            [(k, v) for k, v in day_of_week_posts.items()],
            key=lambda t: t[0],
            reverse=False,
        )
        sorted_day_of_week = [
            (calendar.day_name[k], v) for k, v in sorted_day_of_week_number
        ]

        results["day_of_week"] = sorted_day_of_week

        # Sort weekly users
        sorted_user_posts_monthly = [
            {
                "month": w["month"],
                "users": sorted(
                    [(user_names[k], v) for k, v in w["users"].items()],
                    key=lambda t: t[1],
                    reverse=True,
                ),
            }
            for w in user_posts_monthly
        ]
        user_posts_monthly_final = []
        for w in sorted_user_posts_monthly[:-1]:
            month_dict = {"month": w["month"]}
            placement = []
            for u in w["users"]:
                if not len(placement) or placement[-1]["count"] != u[1]:
                    # Only get the top 3
                    if len(placement) >= 3:
                        break
                    placement.append({"count": u[1], "users": []})
                placement[-1]["users"].append(u[0])

            month_dict["placement"] = placement
            user_posts_monthly_final.append(month_dict)
        results["user_posts_monthly"] = user_posts_monthly_final

        user_posts_monthly_standings = {
            "month": sorted_user_posts_monthly[-1]["month"],
            "users": [],
        }
        for u in sorted_user_posts_monthly[-1]["users"]:
            users = user_posts_monthly_standings["users"]
            if not len(users) or users[-1]["count"] != u[1]:
                users.append({"count": u[1], "users": []})
            users[-1]["users"].append(u[0])

        results["user_posts_monthly_standings"] = user_posts_monthly_standings

        # Add top users
        sorted_user_posts = sorted(
            [(k, v) for k, v in user_posts.items()],
            key=lambda t: len(t[1]),
            reverse=True,
        )
        results["top_users"] = [
            {
                "name": user_names[sorted_user_posts[i][0]],
                "num_posts": len(sorted_user_posts[i][1]),
            }
            for i in range(len(sorted_user_posts))
        ]

        # Add longest streak
        longest_streak = ([None], 0)
        for user_id, posts in user_posts.items():
            user_name = user_names[user_id]
            current_streak = [user_name, 0]
            current_day = None
            for post in posts:
                day = post.created_at.date()
                if day != current_day:
                    if current_day == None or day - timedelta(days=1) != current_day:
                        current_streak[1] = 0
                    current_streak[1] += 1
                    if current_streak[1] == longest_streak[1]:
                        longest_streak[0].append(user_name)
                    elif current_streak[1] > longest_streak[1]:
                        longest_streak = ([user_name], current_streak[1])

                    current_day = day

        # Add top emoji givers
        sorted_user_emojis = sorted(
            [(user_names[k], v) for k, v in user_reactions_count.items()],
            key=lambda t: t[1],
            reverse=True,
        )

        results["emojis"] = [e for e in sorted_emojis if e["count"] > 5]
        results["general_statistics"] = {
            "total_posts": len(timestamps),
            "top_emoji_giver": sorted_user_emojis[0]
            if len(sorted_user_emojis) > 0
            else None,
            "total_emojis": total_emojis,
            "longest_streak": longest_streak,
            "top_emoji": sorted_emojis[0],
        }
        with open("../src/static/assets/workouts.json", "w") as fp:
            json.dump(results, fp)

        user = client.get_user(543581178830127114)
    except Exception as e:
        raise e
    finally:
        pass
    await client.close()


"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
"""


client.run(API_TOKEN)
