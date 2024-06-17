import requests
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391") # to connect with the website or the api page
response.raise_for_status()
data = response.json() 
print(data)