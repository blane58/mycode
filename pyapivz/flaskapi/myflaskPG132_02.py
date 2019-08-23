#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/guest/<guest>")
def hello_guest(name):
    return f"Hello guest, {guest}; glad you could join us"

@app.route("/admin/")
def hello_admin(admin):
    return f"Hello admin"

@app.route("/hello/")
def hello(name):
    return f"Hello {name}"

app.route("/hello/<name>")
def hello(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest, guest=name"))

if __name__ == "__main__":
    #app.run(port=5006, debug=True)  # DEBUG mode
    app.run(port=5006)
