from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb0af4d2e9245e06afd098a182c0c0a28"
# Your Auth Token from twilio.com/console
auth_token  = "597d45e7007c68adb4c281057b02d6ac"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201111271428",
    from_="+12566676154",
    body="Hello from Udacity Python!")

print(message.sid)