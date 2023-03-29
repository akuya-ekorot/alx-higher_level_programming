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

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the private property self

        The setter method checks whether the value passed is an integer and
        not less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
