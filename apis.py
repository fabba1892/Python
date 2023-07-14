# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import asyncio
from dotenv import load_dotenv

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
messages = client.messages.list()


async def delete_all_messages():
    messages =  client.messages.list() #await
    for message in messages:
        print(f"Would have deleted {message.sid}")
        # await message.remove()

print("Starting program")
asyncio.run(delete_all_messages())
print("Done!")

#  make sure the acount and token is secure
# # Download the helper library from https://www.twilio.com/docs/python/install
# from datetime import datetime
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# messages = client.messages.list(
#                                date_sent=datetime(2016, 8, 31, 0, 0, 0),
#                                from_='+15017122661',
#                                to='+15558675310',
#                                limit=20
#                            )

# for record in messages:
#     print(record.sid)
