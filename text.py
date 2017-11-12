# Michael Benos (mtb9ps)

# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACdcf60d519651d1b8ad9e4b9c324e1887"
auth_token = "d5e772c075ca0480221ba15b7df649da"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+18049722051",
    from_="+18044094726",
    body="It is time to start your daily therapy!")