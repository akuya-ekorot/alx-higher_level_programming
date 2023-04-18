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

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        dictionaries = []

        for obj in list_objs:
            dictionaries.append(obj.to_dictionary())

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(dictionaries, f)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps([x for x in list_dictionaries])
