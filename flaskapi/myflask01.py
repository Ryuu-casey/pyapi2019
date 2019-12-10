#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "This is a test of Caseys flask script!"


if __name__ == "__main__":
    app.run(port=5006)
    # app.run(port=5006, debug=True) # DEBUG MODE
