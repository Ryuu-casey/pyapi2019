#!/usr/bin/python3

import yaml


def main():
    yammyfile = open("myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    yammyfile.close()

    print(pyyammy)

    pyyammy[0]['apps'].append('minecraft')

    print(pyyammy)

    yammyfile2 = open("myYAML.yml", "w")

    yaml.dump(pyyammy, yammyfile2)

    yammyfile2.close()


main()
