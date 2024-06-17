from flask import Flask
import functools

app = Flask(__name__)
# first we need to set the environmental variable to the name of the file we are working with 
# to do that in the terminal type :  $env:FLASK_APP="hello.py"
# then in the terminal type: flask run      
# or alternatively we can use: if __name__ == "__main__":
#                                    app.run(debug=True)



def make_bold(func): # creatid a dcorating function to make text bold
    @functools.wraps(func)  # it is important to use this line By applying functools.wraps, we ensure that the decorated functions retain their original names, avoiding the endpoint conflict.
    def to_make_bold_func(*args, **kwargs):
        return f"<b> {func(*args, **kwargs)} </b>"
    return to_make_bold_func

def make_emph(func): # creatid a dcorating function to make text bold
    @functools.wraps(func)  # it is important to use this line By applying functools.wraps, we ensure that the decorated functions retain their original names, avoiding the endpoint conflict.
    def emph(*args, **kwargs):
        return f"<em> {func(*args, **kwargs)} </em>"
    return emph

def make_underline(func): # creatid a dcorating function to make text bold
    @functools.wraps(func)
    def under(*args, **kwargs):
        return f"<u> {func(*args, **kwargs)} </u>"
    return under

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"\
        '<p> such a cute kitty<p>'\
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWEzdWh4dW1uYWZlZHU1aThjbXB6YXlvcThvcW94ZGhlaHpnMmlkYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cfuL5gqFDreXxkWQ4o/giphy.gif'/>"

@app.route("/test")
@make_bold
@make_underline
@make_emph
def test():
    return "just testing"

@app.route("/user/<name>/<int:age>")
@make_bold
@make_underline
@make_emph
def user_age(name,age):
    return f"hello {name} you are {age} years old"

@app.route("/<path:name>") # we use <> to extract this part of the url as a variable then we use it as an input to th the func we can use path or str or int to specify the type the default is str
def hello_name(name):
    return f"hello {name}"





if __name__ == "__main__":
    app.run(debug=True)