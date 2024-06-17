import requests
from datetime import date, timedelta, datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# API_key = "Z1VG7F533G54F9WI"

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol" : STOCK,
#     "apikey": API_key
# }
# response = requests.get("https://www.alphavantage.co/query",params= parameters) # to connect with the website or the api page
# response.raise_for_status()
# data = response.json()["Time Series (Daily)"] 

today = date.today()
#print(today.weekday())
# if today.weekday() == 0:
#     yesterday = today - timedelta(days = 3) # to get yesterday's date
#     daybefore = today - timedelta(days = 4)
# elif today.weekday() == 1:
#     yesterday = today - timedelta(days = 1) # to get yesterday's date
#     daybefore = today - timedelta(days = 3)
# elif 1 < today.weekday() <= 4:
#     yesterday = today - timedelta(days = 1) # to get yesterday's date
#     daybefore = today - timedelta(days = 2)
# else:
#     pass
# # tmedelta is used to sustract any time of any kind hours days anything
# yesterday = today - timedelta(days = 1) # to get yesterday's date
# daybefore = today - timedelta(days = 5)
# yesterday_string = datetime.strftime(yesterday, '%Y-%m-%d') # to convert the date to a string of any format this is a method in the datetime metod of datetime class
# daybefore_string = datetime.strftime(daybefore, '%Y-%m-%d')

# # print(today)
# # print(yesterday)

# # to extract the data from the response we got from our request 
# yesterday_closing = float(data[yesterday_string]["4. close"])
# daybefore__closing = float(data[daybefore_string]["4. close"])
# print(type(daybefore__closing))

# closing_percent = (yesterday_closing - daybefore__closing) * 100 / (yesterday_closing)
closing_percent = -0.655555
if closing_percent > 0.05 or closing_percent < -0.05:
    print("get news")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(closing_percent):
    news_api = "6eddeee6804646e8b8c55a7f108555d2"



    parameters = {
        "q": "tesla",
        "from" : today - timedelta(days = 2),
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": news_api
    }
    response1 = requests.get("https://newsapi.org/v2/everything?",params= parameters) # to connect with the website or the api page
    response1.raise_for_status()
    news = response1.json()["articles"][:3]
    messages=[]
    for i in news:
        message = f"tesla stock changed {closing_percent}\n here are some news author: {i["author"]}\n title: {i["title"]}\ncontent:{i["content"]}"
        messages.append(message)
        print(message)
        sms(message)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# account_sid =  "ACd7b54eca77d24e78b7b26624c70f32a3"
# auth_token = "ACd7b54eca77d24e78b7b26624c70f32a3"
def sms(message):
    account_sid = "ACd7b54eca77d24e78b7b26624c70f32a3"
    auth_token = "ACd7b54eca77d24e78b7b26624c70f32a3"

    phone_number = "+14255377471"

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_=phone_number,
                        to='+201110888811'
                    )

    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

get_news(0.6666666666)
