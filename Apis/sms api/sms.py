###### twillo for sending sms#######
import os
from twilio.rest import Client

# WE USE the command gci Env:  to show the Env variables
# To set an environment variable, you can use the $env: prefix: 
# $env:tillio_account_id = "ACd7b54eca77d24e78b7b26624c70f32a3" (in powershell)
# export tillio_account_id = "ACd7b54eca77d24e78b7b26624c70f32a3"  (in bash )

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('tillio_account_id')
auth_token = os.environ.get('tillio_auth_token')

phone_number = "+14255377471"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I love you Safia <3 with I not Y",
                     from_=phone_number,
                     to='+201128576046'
                 )

print(message.status)

# account_sid =  "ACd7b54eca77d24e78b7b26624c70f32a3"
# auth_token = "17148dd4e046c2ab78adfbde9d0e64f9"


