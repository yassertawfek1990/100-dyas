from flask import Flask, render_template
import requests


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


@app.route('/contact')
def to_contact():
    return render_template("contact.html")

@app.route('/<int:n>')
def posting(n):
    return render_template("post.html",post = data[n-1])
if __name__ == "__main__":
    app.run(debug=True)

