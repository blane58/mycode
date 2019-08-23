#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# route() function of the Flask class is a decorator; tells the application which URL should call the associated function

@app.route("/hello/<name>")
@app.route("/")
def hello(name):
    #with open("helloworld.txt", "w") as hello:
    #    hello.write("I am makin flask apps!")
    #return "File Created"
    return f"Hello {name}; glad you could join us"

@app.route("/goodbye/<name>")
def goodbye():
    #with open("goodbye.world", "w") as goodbye:
    #    goodbye.write("Later on dudes!")
    #return "File Created"
    return f"Goodbye {name}; Sorry to see you leave, but see you next time"

if __name__ == "__main__":
    #app.run(port=5006)  # runs the application
    app.run(port=5006, debug=True)  # DEBUG mode

