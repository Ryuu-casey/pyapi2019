#!/user/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"


@app.route("/")
@app.route("/start")
def start():
    return render_template("postmaker.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"
    elif request.method == "GET":
        if request.args.get("nm"):
            user = request.args.get("nm")
        else:
            user = "defaultuser"
    return redirect(url_for("success", name=user))


if __name__ == "__main__":
    app.run(port=5006)
