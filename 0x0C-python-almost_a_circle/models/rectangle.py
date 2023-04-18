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

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle instance
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

    def update(self, *args, **kwargs):
        """Updates the values of the instance
        """
        attributes = ["id", "width", "height", "x", "y"]

        if args:

            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def display(self):
        """Prints in stdout the rectangle instance with character #
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def area(self):
        """Returns the area of the rectangle
        """
        return self.__width * self.__height

    @property
    def width(self):
        """Getter for private property __width
        The setter takes in the parameter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for private property __height
        The setter takes in the parameter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 1:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for private property __x
        The setter takes in the parameter x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for private property __y
        The setter takes in the parameter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
