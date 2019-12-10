#!/usr/bin/python3

import pandas as pd


def main():
    # Create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # Create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    # Export to json
    # Do not include index number
    ciscodf.to_json("combined_ciscodata.json", orient="records")

    # Export to csv
    # Do not include index number
    ciscodf.to_csv("combined_ciscodata.csv", index=False)

    # Export to Excel
    # Do not include index number to xls
    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    # do not include index number to xlsx
    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)

    # Create a python dictionary
    # Do not include index number
    x = ciscodf.to_dict(orient='records')
    print(x)


if __name__ == "__main__":
    main()
