#!/usr/bin/python3
"""contains the function inherits_from"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class that inherited (directly
 or indirecty) from the specified class; otherwise false"""

    return isinstance(obj, a_class) and not (type(obj) == a_class)
