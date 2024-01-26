import os
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
    "for",
    "if",
    "in",
    "into",
    "is",
    "it",
    "no",
    "not",
    "of",
    "on",
    "or",
    "such",
    "that",
    "the",
    "their",
    "then",
    "there",
    "these",
    "they",
    "this",
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
        results = {"updated": str(datetime.today()), "since": str(since)}

        # Get all user name and nick names into a dict
        user_names = {}
        ch = client.get_channel(workouts_channel_id)
        guild = ch.guild
        async for member in guild.fetch_members():
            user_names[member.id] = member.nick or member.display_name

        user_posts = {}
        posts_by_months = {}
        timestamps = []
        dates = []
        user_reactions_count = {}
        day_of_week_posts = {}
        total_emojis = 0
        popular_emojis = {}
        words = {}
        async for m in ch.history(after=since, limit=None):
            if len(m.attachments):
                user = m.author
                user_id = user.id
                if user_id not in user_posts:
                    user_posts[user_id] = []

                user_posts[user_id].append(m)
                timestamp = calendar.timegm(m.created_at.utctimetuple())
                timestamps.append(timestamp)
                current_day = m.created_at.date()

                # Add dates
                if not len(dates) or dates[-1][0] != str(current_day):
                    dates.append([str(current_day), 0])
                dates[-1][1] += 1

                # Add day of week calculation
                weekday = m.created_at.weekday()
                if weekday not in day_of_week_posts:
                    day_of_week_posts[weekday] = 0
                day_of_week_posts[weekday] += 1

                # Add message content to word bubble
                for word in m.content.split(" "):
                    if word not in stop_words and not word.startswith("<@"):
                        if word not in words:
                            words[word] = 0
                        words[word] += 1

                for reaction in m.reactions:
                    emoji = reaction.emoji
                    emoji_id = emoji if isinstance(emoji, str) else emoji.id
                    if emoji_id not in popular_emojis:
                        popular_emojis[emoji_id] = {
                            "count": 0,
                            "emoji": emoji if isinstance(emoji, str) else emoji.url,
                            "is_url": not isinstance(emoji, str),
                        }
                    popular_emojis[emoji_id]["count"] += reaction.count
                    total_emojis += reaction.count
                    """
                    # Commented out for now because it takes too long
                    async for user in reaction.users():
                        if user.id not in user_reactions_count:
                            user_reactions_count[user.id] = 0
                        user_reactions_count[user.id] += 1
                    """

        # Add words
        results["words"] = words

        # Add timestamps
        results["timestamps"] = timestamps
        results["dates"] = dates

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
