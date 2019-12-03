#!/usr/bin/python3

import json
import urllib.request

NEO = "https://api.nasa.gov/neo/rest/v1/feed?api_key="


def main():
    # Get my API key
    with open(r"C:\Users\Student\Documents\nasacreds.txt", "r") as nc:
        myapikey = nc.read()

    neoresp = urllib.request.urlopen(NEO + myapikey)
    neojson = neoresp.read().decode("utf-8")
    neopy = json.loads(neojson)

    for nasadate in neopy["near_earth_objects"]:
        print(nasadate)
        for asteroids in neopy["near_earth_objects"][nasadate]:
            print("    The human name is: ", asteroids["name"])
            print("    The Astronomical ID is: ", asteroids["id"])
            print("    Potentially hazardous: ", asteroids["is_potentially_hazardous_asteroid"])
            print("    Orbits: ", asteroids["close_approach_data"][0]["orbiting_body"])
            print()


if __name__ == "__main__":
    main()
