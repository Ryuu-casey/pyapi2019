#!/usr/bin/python3

import yaml


def main():
    yammyfile = open("myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)


if __name__ == "__main__":
    main()
