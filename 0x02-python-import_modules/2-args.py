#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv) - 1
    print("{0} arguement".format(length), end="")

    if length == 0:
        print("s.")
    else:
        if length == 1:
            print(":")
        else:
            print("s:")

        for i in range(length):
            print("{0}: {1}".format(i + 1, sys.argv[i + 1]))
