from flask import Flask

## WSGI Application
app=Flask(__name__) # It creates an instance of the Flask class, which will be your WSGI (web server gateway interface) application.

@app.route("/")
def welcome():
    return "Wlcome to Flask app, This is an amazing app"

@app.route("/index")
def index():
    return "welcome to index page"


if __name__ =="__main__":
    app.run(debug=True)