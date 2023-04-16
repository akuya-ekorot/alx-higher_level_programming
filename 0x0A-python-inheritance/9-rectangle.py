#!/usr/bin/python3
"""contains the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits BaseGeometry to form a rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[{}] {}/{}".format(
            self.__class__.__name__,
            self.__width,
            self.__height
        )

    def area(self):
        return self.__height * self.__width
