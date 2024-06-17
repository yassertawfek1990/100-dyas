from flask import Flask, render_template
import datetime as dt
import requests
app = Flask(__name__)
# first we need to set the environmental variable to the name of the file we are working with 
# to do that in the terminal type :  $env:FLASK_APP="hello.py"
# then in the terminal type: flask run      
# or alternatively we can use: if __name__ == "__main__":
#                                    app.run(debug=True)



### BEST WAY TO EDIT HTML FILE open the page in chrome the go to more tools then developer tools then console then write document.body.contentEditable=true
## now we can edit any text remove any parts then we need to click ctrl + s to save the final page after editing then use it in oure templates folder
def get_gender(a_name):
    url = f"https://api.genderize.io?name={a_name}"
    response = requests.get(url) # to connect with the website or the api page
    response.raise_for_status()
    data = response.json() # to extract the data from the response we got from our request 
    return data["gender"]

def get_age(a_name):
    url = f"https://api.agify.io?name={a_name}"
    response = requests.get(url) # to connect with the website or the api page
    response.raise_for_status()
    data = response.json() # to extract the data from the response we got from our request 
    return data["age"]




@app.route("/")

def hello():
    the_year = dt.datetime.now().year
    return render_template("index.html",year = the_year)

@app.route("/guess/<name>")

def guessing(name):
    return render_template("datas.html",naming = name,gender = get_gender(name),age = get_age(name))

@app.route("/blog")
def blogging():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391") # to connect with the website or the api page
    response.raise_for_status()
    data = response.json() 
    return render_template("blog.html",blogs = data)

if __name__ == "__main__":
    app.run(debug=True)