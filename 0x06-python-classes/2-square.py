#!/usr/bin/python3
"""This module contains the class Square
"""


class Square:
    """This is a square class
    """

    def __init__(self, size=0):
        """initializer function"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
