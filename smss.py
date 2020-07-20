from twilio.rest import Client
def sms():
    account_sid ="" # Put your Twilio account SID here
    auth_token ="" # Put your auth token here

    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(
            to="", # Put your cellphone number here
            from_="", # Put your Twilio number here
            body="")
        