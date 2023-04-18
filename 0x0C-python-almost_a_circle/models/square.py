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
