#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# Documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://anapioficeandfire.com/api/books"


def main():
    # Send HTTPS GET to the API of ICE and FIRE books resource
    gotresp = requests.get(AOIF_BOOKS)

    # Decode the response
    got_dj = gotresp.json()

    # Print the response
    # Using pretty print so we can read it
    pprint.pprint(got_dj)


if __name__ == "__main__":
    main()
