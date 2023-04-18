#!/usr/bin/python3
"""module contains class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.size)

    def update(self, *args, **kwargs):
        """Updates the values of the instance
        """
        attributes = ["id", "size", "x", "y"]

        if args:

            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    @property
    def size(self):
        """Getter for the private property size
        Setter takes in the parameter size
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")

        self.width = self.height = value
