#!/usr/bin/python3
"""
script that adds all arguements to Python list, and then saves them to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = sys.argv[1:]
filename = "add_item.json"

try:
    loaded_list = load_from_json_file(filename)
    loaded_list += argv
    save_to_json_file(loaded_list, filename)
except Exception:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(argv, f)
