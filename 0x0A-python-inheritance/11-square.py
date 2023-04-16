#!/usr/bin/python3
"""module contains the class Square which inherits Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits rectangle to make a square"""

    def __init__(self, size):
        super(Rectangle, self).integer_validator("size", size)
        super().__init__(size, size)
