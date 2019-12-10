#!/usr/bin/python3

import pandas as pd


def main():
    flightcsv = pd.read_csv("airline_flights.csv")

    # Orginize data by origin and destination airport
    flightcsv_tofrom = flightcsv.groupby(['ORG_AIR', 'DEST_AIR']).size()
    print(flightcsv_tofrom.head())

    # Display the number of flights between Huston (IAH)
    # And Atlanta (ALT) in both directions
    print("\nFlight from ALT to IAH and IAH to ALT")
    print(flightcsv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])

    # Display first 5 entries of the flightcsv dataframe
    print(flightcsv_tofrom.head())


if __name__ == "__main__":
    main()
