#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# Documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://anapioficeandfire.com/api"


def main():
    # Send HTTPS GET to the API of ICE and FIRE
    gotresp = requests.get(AOIF)

    # Decode the response
    got_dj = gotresp.json()

    # Print the response
    print(got_dj)


if __name__ == "__main__":
    main()
