from numpy import *
from twilio.rest import TwilioRestClient


# my_array = array([1, 2, 3, 4, 2, 1, 3, 4, 5, 3, 1, 3, 4, 5, 5])
# print(unique(my_array))

customers = array([4326409456, 4322386131, 8064770982, 4326409456, 4322386131, 8064770982, 8064770982, 4322386131])
cleaned_customers = unique(customers)

account_sid = "ACd0bd6cb95287b16d71680717cef25118"
auth_token = "ab69cac28df6d31c85ea68a43c331ada"
client = TwilioRestClient(account_sid, auth_token)

for customer in cleaned_customers:
    message = client.messages.create(
        body = "Python 3 says hi from my first Twilio app!",
        to = "+1{}".format(customer),
        from_ = "+14322428216"
    )

print(message.sid)