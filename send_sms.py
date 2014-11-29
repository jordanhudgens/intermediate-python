# To install, run the following commands:
# python3.4 -m pip install twilio
# pip3 install socksipy-branch

from twilio.rest import TwilioRestClient

# You will get these from your Twilio dashboard
account_sid = "REPLACE WITH YOUR TWILIO ACCOUNT SID"
auth_token = "REPLACE WITH YOUR AUTH TOKEN"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    # Contents you want sent in the SMS message
    body = "Python 3 says hi form my first Twilio app!",

    # For the phone numbers make sure incorporate the country code, for US numbers it will be '+1'
    to = "REPLACE WITH THE NUMBER YOU WANT TO SEND THE SMS TO",
    from_ = "REPLACE WITH YOUR TWILIO PHONE NUMBER")

print(message.sid)