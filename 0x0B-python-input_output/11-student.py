#!/usr/bin/python3
"""module contains class Student"""


class Student():
    """class Student that defines a student by first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__ = {k: json.get(k, v) for k, v in self.__dict__.items()}

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student instance"""

        if attr is None:
            return self.__dict__

        filtered = {}

        for a in attr:
            try:
                filtered[a] = self.__dict__[a]
            except Exception:
                pass

        return filtered
