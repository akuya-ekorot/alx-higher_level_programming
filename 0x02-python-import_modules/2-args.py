#!/usr/bin/python3
import sys

length = len(sys.argv) - 1
print("{0} arguements".format(length), end="")

if length == 0:
    print(".")
else:
    print(":")
    for i in range(length):
        print("{0}: {1}".format(i + 1, sys.argv[i + 1]) )

