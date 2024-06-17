from flask import Flask, render_template

app = Flask(__name__)
# first we need to set the environmental variable to the name of the file we are working with 
# to do that in the terminal type :  $env:FLASK_APP="hello.py"
# then in the terminal type: flask run      
# or alternatively we can use: if __name__ == "__main__":
#                                    app.run(debug=True)



### BEST WAY TO EDIT HTML FILE open the page in chrome the go to more tools then developer tools then console then write document.body.contentEditable=true
## now we can edit any text remove any parts then we need to click ctrl + s to save the final page after editing then use it in oure templates folder

@app.route("/")

def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)