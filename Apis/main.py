import requests
import datetime as dt
response = requests.get("http://api.open-notify.org/iss-now.json") # to connect with the website or the api page
response.raise_for_status()
data = response.json() # to extract the data from the response we got from our request 
print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude,longitude)

print(iss_position)


parameters = {
    "lat": 29.961002 ,
    "lng": 30.952331,
    "formatted": 0
}
response2 = requests.get("https://api.sunrise-sunset.org/json",params= parameters) # to connect with the website or the api page
response2.raise_for_status()
data2 = response2.json() # to extract the data from the response we got from our request 

# thats how to access the data via chrome https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0  we add ? then the parameters
print(data2)
sunrise = data2["results"]["sunrise"]
sunset = data2["results"]["sunset"]
print(sunrise,sunset)

# split to extract the hour only
sunrise_hour = sunrise.split("T") # retuens list
sunrise_hour = sunrise_hour[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)
print(dt.datetime.now().hour)