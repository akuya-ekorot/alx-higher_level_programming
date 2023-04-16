#!/usr/bin/python3
"""module contains the function add_attribute"""


def add_attribute(obj, name, value):
    """adds attributes to objects"""
    if hasattr(obj, "__dict__") or (hasattr(obj.__class__, "__slots__") and
                                    name in obj.__class__.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("cant add new attribute")
