import smtplib

my_email = "fokak908070@gmail.com"
app_password = "ixpw empl cdam pxha" # the password we create from the email provider by making a new app in i from security options
recieving_email = "yasser.tawfek@optad360.com"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls() # to make the message we send encrypted and could not be read by an hacker
    connection.login(user= my_email, password= app_password )
    connection.sendmail(from_addr= my_email , to_addrs= recieving_email, msg="Subject: you can choose whatever subject \n\n And here is the body") # it is normal to shown sent as bcc
