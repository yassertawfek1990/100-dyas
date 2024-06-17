from flask import Flask
import random
app = Flask(__name__)
# first we need to set the environmental variable to the name of the file we are working with 
# to do that in the terminal type :  $env:FLASK_APP="hello.py"
# then in the terminal type: flask run      
# or alternatively we can use: if __name__ == "__main__":
#                                    app.run(debug=True)


number = random.randint(0,9)

@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:n>")
def check(n):
    if n == number:
        return "<h1 style='color: green'>You found me</h1>"\
        "<img src='https://media.giphy.com/media/W5ZUxqXT1lmiysXsDE/giphy.gif?cid=ecf05e4743pe02unpo0311gwezfwziv2rxpi37w1isqcj1qa&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"
    elif n < number:
        return "<h1 style='color: blue'>Too low</h1>"\
        "<img src='https://media.giphy.com/media/yJCm3rCR3SPaavovWn/giphy.gif?cid=ecf05e47qxtr79sy9497o3zbtx6xoq3hd0kz6q4cscqfse8v&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"
    else:
        return "<h1 style='color: red'>Too high</h1>"\
        "<img src ='https://media.giphy.com/media/vexp4GOO5r0OI/giphy.gif?cid=790b7611wzxvpnx0mplzls50qwa4qqv2psv6j12pp6e2tf1h&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"
    

if __name__ == "__main__":
    app.run(debug=True)