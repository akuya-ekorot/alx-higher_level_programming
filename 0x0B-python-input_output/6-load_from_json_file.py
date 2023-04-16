#!/usr/bin/python3
"""module contains the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
