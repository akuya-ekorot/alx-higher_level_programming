#!/usr/bin/python3
"""module contains the class Base
"""
import json


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns json representation of list_dictionaries"""
        return json.dumps([x for x in list_dictionaries])
