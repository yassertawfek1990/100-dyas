from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


def email(message):
    my_email = "fokak908070@gmail.com"
    app_password = "ixpw empl cdam pxha" # the password we create from the email provider by making a new app in i from security options
    recieving_email = "yasser.tawfek@optad360.com"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls() # to make the message we send encrypted and could not be read by an hacker
        connection.login(user= my_email, password= app_password )
        connection.sendmail(from_addr= my_email , to_addrs= recieving_email, msg=message) # it is normal to shown sent as bcc


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
data =  response.text

soup = BeautifulSoup(data, "lxml")

price = soup.find('span', class_='a-offscreen').text
print(price)
price_int = float(price[1:])

if price_int < 100:
    message = f"Subject: Cooker with good price \n\n the cooker reached Good price and it si now with {price_int}$"
    email(message)

