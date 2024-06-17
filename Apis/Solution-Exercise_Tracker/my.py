import requests
from datetime import datetime
import os


# Many web services that require authentication accept HTTP Basic Auth. This is the simplest kind, and Requests supports it straight out of the box.

# Making requests with HTTP Basic Auth is very simple:

# from requests.auth import HTTPBasicAuth
# basic = HTTPBasicAuth('user', 'pass')
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)


application_keys = "2a5f8ec8cfd315a2d407fd5905cb2382"
Message = "not found"
domain = "https://trackapi.nutritionix.com//v2/natural/exercise"
header = {
    "x-app-id": os.environ.get("APP_ID", Message),
    "x-app-key": application_keys

}
# que = input("what have you done :)\n")
parameters_get= {
    "query":"I ran 2 miles"
}

response = requests.post(url=domain,json=parameters_get, headers=header)

data = response.json()

dates = datetime.strftime(datetime.now().date(),"%d/%m/%Y")
hours = datetime.now().time().strftime("%X")

# print(hours)
cal = data["exercises"][0]["nf_calories"]
dur = data["exercises"][0]["duration_min"]
ex = data["exercises"][0]["user_input"]

# print(cal)
username = "425f4bfb948586b04a742ceca19e93cb"
project_name = "myWorkouts"
sheetName = "workouts"
post_domain = f"https://api.sheety.co/{username}/{project_name}/{sheetName}"

parameters_post = {
    "workout":{
    "date": dates ,
        "time": hours,
        "exercise": ex.title(),
        "duration": str(dur),
        "calories": str(cal)
    }
}
header = {"Authorization": "Basic eWFzc2VyMTk5MDpZYXNzZXIxOTkw"}
post_response = requests.post(url=post_domain,json=parameters_post,headers=header)
print(post_response.text)