#!/user/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for

app = Flask(__name__)
app.secret_key = "any random string"


# red letter media

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return "Logged in as " + username + "<br>" + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    return """
    <form action = "" method = "post">\
        <p><input type = text name = username></p>\
        <p><input type = submit value = Login></p>\
    </form>\
"""


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5006)
