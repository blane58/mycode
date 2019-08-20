#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# route() function of the Flask class is a decorator; tells the application which URL should call the associated function

@app.route("/hello/")
@app.route("/")
def hello_world():
    with open("helloworld.txt", "w") as hello:
        hello.write("I am makin flask apps!")
    return "File Created"

@app.route("/goodbye/")
def goodbye_world():
    with open("goodbye.world", "w") as goodbye:
        goodbye.write("Later on dudes!")
    return "File Created"

if __name__ == "__main__":
    app.run(port=5006)  # runs the application
    # app.run(port=5006, debug=True)  # DEBUG mode

