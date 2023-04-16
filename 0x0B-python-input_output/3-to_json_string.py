#!/usr/bin/python3
"""module contains the function to_json_string"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object (string)"""

    return json.dumps(my_obj)
