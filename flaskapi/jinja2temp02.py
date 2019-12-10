#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/<username>")
def index(username):
    return render_template("helloname.html", name=username)


if __name__ == "__main__":
    app.run(port=5006)
