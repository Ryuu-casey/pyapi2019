#!/usr/bin/python3

from flask import Flask
import json
import random

app = Flask(__name__)


@app.route("/poems")
def send():
    with open('../poem/poems.json') as poems:
        jpoems = json.load(poems)
    return str(random.choice(list(jpoems.values())))


if __name__ == "__main__":
    app.run(port=5006)
