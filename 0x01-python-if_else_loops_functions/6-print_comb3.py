#!/usr/bin/python3

for i in range(9):
    for j in range(10):
        if j > i:
            if i != 8:
                print(f"{i}{j}", end=", ")
            else:
                print(f"{i}{j}")
