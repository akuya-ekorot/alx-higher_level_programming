#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1

    print("{0} argument".format(length), end="")

    if length == 0:
        print("s.")
    else:
        if length == 1:
            print(":")
        else:
            print("s:")

        for i in range(length):
            print("{0}: {1}".format(i + 1, argv[i + 1]))
