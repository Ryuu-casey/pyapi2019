#!/usr/bin/python3

import requests

POKEMONAPI = "https://pokeapi.co/api/v2/pokemon/"


def main():
    poke = requests.get(POKEMONAPI)
    pokejson = poke.json()
    # print(pokejson)
    for abl in pokejson["results"]:
        print(abl["name"])


if __name__ == "__main__":
    main()
