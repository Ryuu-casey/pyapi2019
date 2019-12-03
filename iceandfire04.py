#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# Documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://anapioficeandfire.com/api/characters"


def main():
    # Ask user for input
    got_charToLookup = input("What is the name of the character we should lookup? ")

    # Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + "?name=" + got_charToLookup)

    # Decode the response
    got_dj = gotresp.json()

    print(got_dj)
    print(f"The character {got_charToLookup} has the URL: {got_dj[0]['url']}")
    print(f"{got_charToLookup} belongs to the house: {got_dj[0]['allegiances']}")
    pprint.pprint(f"The character appears in the following books: {got_dj[0]['books']}")


if __name__ == "__main__":
    main()
