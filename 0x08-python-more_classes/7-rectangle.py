#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """The rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__dict__ = {}
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol * self.__width) + "\n") *
                (self.__height - 1) +
                str(self.print_symbol * self.__width))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def height(self):
        """getter for the private property height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """getter for the private property width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """Returns the rectangle's area"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
