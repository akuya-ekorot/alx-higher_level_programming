#!/usr/bin/python3

for i in range(97, 123):
    if not (chr(i) == "e" or chr(i) == "q"):
        print(f"{chr(i)}", end="")
