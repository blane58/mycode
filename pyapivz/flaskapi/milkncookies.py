#!/usr/bin/python3

from flask import Flask, make_response, request, render_template

## Write some python code (function) that connects to database
## Write some more python code (function) to pull the data from the database

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookies():
    if request.method == "POST":
        user = request.form.get("nm")
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp
    elif request.method == "GET":
        return render_template("index.html")

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f"Welcome back, {name}"

if __name__ == "__main__":
    #app.run(port=5006, host='127.0.0.1')
    app.run(port=5006)






