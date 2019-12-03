#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# Documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_BOOKS = "https://anapioficeandfire.com/api/books"


def main():
    # Send HTTPS GET to the API of ICE and FIRE books resource
    gotresp = requests.get(AOIF_BOOKS)

    # Decode the response
    got_dj = gotresp.json()

    # Loop across response
    for singlebook in got_dj:
        # Display the names of each book
        # All of the below statements do the same thing
        # print(singlebook["name"] + ",", "pages -", singlebook["numberofpages"])
        # print("{}, pages - {}".format(singlebook["name"], singlebook["numberofpages"]))
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # Print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")


if __name__ == "__main__":
    main()
