#!/usr/bin/python3

def main():


    mylist = []
    mylist.append("monday")
    mylist.append("tuesday")
    mylist.append("wednesday")
    mylist.append("thursday")
    #print(mylist)
    #print(mylist[0])
    #print(mylist[3])

    studiomovies = {}

    studiomovies["pixar"] = "toystory"
    studiomovies["universal"] = "jaws"
    studiomovies["paramount"] = "raiders of the lost ark"

    #print(studiomovies)
    #print(studiomovies["paramount"])

    studiomovies["pixar"] = ["toystory", "up"]

    print(studiomovies["pixar"][1])


if __name__ == "__main__":
    main()
