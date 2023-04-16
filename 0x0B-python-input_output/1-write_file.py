#!/usr/bin/python3
"""module contains the function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns no. of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
