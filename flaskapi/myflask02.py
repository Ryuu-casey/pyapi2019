#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    x = 235
    y = 445
    z = 345
    return f"Hello {name} {x} plus {y} multiplied by {z} equals {(x + y) * z}"


@app.route("/bond")
def bond():
    return f"Bond, James Bond 007"


@app.route("/secretagent/<donumber>")
def britishagent(donumber):
    return f"Hello Secret Agent {donumber}. We have an assignment for you."


if __name__ == "__main__":
    app.run(port=5006, debug=True)
