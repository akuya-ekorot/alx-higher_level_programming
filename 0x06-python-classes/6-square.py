#!/usr/bin/python3
"""This module contains the class Square
"""


class Square:
    """This is a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializer function"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Getter method for the private property size

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

    @property
    def position(self):
        """Getter method for the private property position

        The setter method checks whether position is a tuple of 2 positive
        integers"""
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints in stdout the square with the
        character '#'"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("{}".format("\n" * self.__position[1]), end="")
            for i in range(0, self.__size):
                print("{}{}".format((self.__position[0] * " "),
                                    (self.__size * "#")))
