import requests

api_key = "9c775e409a19c01e39a5ff8ad38f59a1"
MY_LAT = 29.961002 # Your latitude
MY_LONG = 30.952331 # Your longitude




paramaters = {
    "lat":MY_LAT ,
    "lon" :MY_LONG,
    "appid": api_key
    # "exclude":

}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?",params=paramaters) # to connect with the website or the api page
response.raise_for_status()
data = response.json()["list"] # to extract the data from the response we got from our request 
weather = [w["weather"] for w in data ][2:6]

umb = False
for i in weather:
    if i[0]["id"] > 700:
        umb = True
        print("bring shorts")
 
if umb == True:
    print("bring shorts")


