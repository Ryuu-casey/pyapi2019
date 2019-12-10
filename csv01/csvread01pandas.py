#!/usr/bin/python3

import pandas


def main():
    # Create a dataframe called superdf from our csv data
    superdf = pandas.read_csv("superbirthday.csv")

    # Display the column names
    print(f"Column names are {', '.join(superdf)}")

    # Uncomment the line below if you need to see what we are looping across
    # orient = 'records' prevents to_dict() from using the index value
    # print(superdf.to_dict(orient='records'))

    for row in superdf.to_dict(orient='records'):
        print(f"\t{row['name']} aka {row['heroname']}, was born in {row['birthday month']}.")

    # Print the total number of lines (span returns (lines, columns))
    print(f"Total lines processed {superdf.shape[0]}")


if __name__ == "__main__":
    main()
