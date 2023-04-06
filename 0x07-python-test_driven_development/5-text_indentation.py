#!/usr/bin/python3
"""This module contains the function text_indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters '.', '?', ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print("{}".format(text)
          .replace(". ", "\n\n")
          .replace("? ", "\n\n")
          .replace(": ", "\n\n"))
