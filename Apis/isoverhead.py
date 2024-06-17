import requests
from datetime import datetime
import smtplib
import time
import threading

def lookup():

    MY_LAT = 29.961002 # Your latitude
    MY_LONG = 30.952331 # Your longitude



    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <=   MY_LAT >= iss_latitude - 5) and (MY_LONG + 5 <= iss_longitude >=  MY_LONG - 5):
            return True
#Your position is within +5 or -5 degrees of the ISS position.

def now():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour > sunset and time_now.hour < sunrise:
         return True 

#If the ISS is close to my current position

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def my_function():
    if lookup() and now():
        my_email = "fokak908070@gmail.com"
        app_password = "ixpw empl cdam pxha" # the password we create from the email provider by making a new app in i from security options
        recieving_email = "yasser.tawfek@optad360.com"
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls() # to make the message we send encrypted and could not be read by an hacker
                connection.login(user= my_email, password= app_password )
                connection.sendmail(from_addr= my_email , to_addrs= recieving_email, msg="Subject: Look Up \n\n The ISS is above you ") # it is normal to shown sent as bcc


def run_periodically():
    while True:
        my_function()
        time.sleep(60)  # Wait for 60 seconds

# Create and start the thread
thread = threading.Thread(target=run_periodically)
thread.daemon = True  # This makes sure the thread will exit when the main program exits
thread.start()



