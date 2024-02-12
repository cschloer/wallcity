from time import time
import logging
import json
import os
import discord
import boto3
import asyncio
from datetime import datetime, timedelta, date
from workouts.script import run_script, client, API_TOKEN

import nest_asyncio

nest_asyncio.apply()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Hard coded
CLOUDFRONT_DIST_ID = "E24W1LKTABLEFV"


async def async_handler(event, context):
    @client.event
    async def on_ready():
        try:
            results = await run_script()

            encoded_string = json.dumps(results).encode("utf-8")
            bucket_name = os.environ.get("BUCKET_NAME", None)
            file_name = "workouts.json"
            s3_path = f"static/assets/{file_name}"

            s3 = boto3.resource("s3")
            s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)

            cloudfront_client = boto3.client("cloudfront")
            response = cloudfront_client.create_invalidation(
                DistributionId=CLOUDFRONT_DIST_ID,
                InvalidationBatch={
                    "Paths": {
                        "Quantity": 1,
                        "Items": ["/*"],
                    },
                    "CallerReference": str(time()).replace(".", ""),
                },
            )
            print("Cloudfront response: ", response)

        except Exception as e:
            print("THERE WAS AN ERROR", e)
            raise e
        finally:
            pass
        await client.close()

    # Put your asynchronous code here
    start_time = datetime.now().time()
    client.run(API_TOKEN)
    current_time = datetime.now().time()
    name = context.function_name
    logger.info(
        f"Cron function {name} started at {str(start_time)} and ended at {str(current_time)}"
    )

    return {"statusCode": 200, "body": {"ok": True}}


def run(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_handler(event, context))


if __name__ == "__main__":
    run(None, None)
