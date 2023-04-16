#!/usr/bin/python3
"""module contains the function from_json_string"""
import json


def from_json_string(my_str):
    """converts from json to python object"""

    return json.loads(my_str)
