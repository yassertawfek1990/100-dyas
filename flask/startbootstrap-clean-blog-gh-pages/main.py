from flask import Flask, render_template,request
import requests
import smtplib


app = Flask(__name__)


response = requests.get("https://api.npoint.io/c790b4d5cab58020d391") # to connect with the website or the api page
response.raise_for_status()
data = response.json()

@app.route('/')
def home():
    return render_template("index.html",all = data)


@app.route('/about')
def to_about():
    return render_template("about.html")



# @app.route('/contact')
# def to_contact():
#     return render_template("contact.html")

@app.route('/contact', methods=["POST","GET"])
def to_contact():
    if request.method == 'POST':
        my_email = "fokak908070@gmail.com"
        app_password = "ixpw empl cdam pxha" # the password we create from the email provider by making a new app in i from security options
        recieving_email = "yessirtawfek@gmail.com"

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls() # to make the message we send encrypted and could not be read by an hacker
            connection.login(user= my_email, password= app_password )
            connection.sendmail(from_addr= my_email , to_addrs= recieving_email, msg=f"Subject: we got a message \n\n his name is {name} his email is {email} his phone is {phone} and the message is {message}") # it is normal to shown sent as bcc

        return render_template("contact.html",submit = True)
    else:
        return render_template("contact.html")

@app.route('/<int:n>')
def posting(n):
    return render_template("post.html",post = data[n-1])
if __name__ == "__main__":
    app.run(debug=True)

