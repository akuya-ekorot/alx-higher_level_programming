#!/usr/bin/python3
"""module contains class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for private property __width
        The setter takes in the parameter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Getter for private property __height
        The setter takes in the parameter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Getter for private property __x
        The setter takes in the parameter x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Getter for private property __y
        The setter takes in the parameter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
