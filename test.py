from twilio.rest import TwilioRestClient

account_sid = "ACaa7b80f486842e702fd49071cf7a2324" # Your Account SID from www.twilio.com/console
auth_token  = "425da762ac1d795bb3ab4d50f9c59373"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+32471397440",    # Replace with your phone number
    from_="+32460207366") # Replace with your Twilio number

print(message.sid)