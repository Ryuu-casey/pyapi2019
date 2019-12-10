#!/usr/bin/python3

import json


class Mariokartplayer:
    def __init__(self, name, karttype):
        with open("mkmkcjson.json") as mkd:
            stats = json.load(mkd)
        self.name = name
        self.karttype = karttype
        self.score = 0
        self.item = None
        self.type = stats[name]["type"]

    # This is for display when someone tries to print the object
    def __str__(self):
        return self.name

    def scorechange(self, condition):
        if condition == "coin":
            self.score += 10
        elif condition == "finishline":
            self.score += 100
        elif condition == "pushopponent":
            self.score += 25
        else:
            self.score += 5


def main():
    print("learning about classes with mario kart")
    player1 = Mariokartplayer("Yoshi", "50cc")

    print(player1)
    print(player1.name)
    print(player1.karttype)
    print(player1.score)
    print(player1.item)
    print(player1.type)

    player1.scorechange("coin")
    print(player1.score)

    player1.scorechange("pushopponent")
    print(player1.score)

    player1.scorechange("finishline")
    print(player1.score)

    player1.scorechange("herbaflober")
    print(player1.score)


if __name__ == "__main__":
    main()
