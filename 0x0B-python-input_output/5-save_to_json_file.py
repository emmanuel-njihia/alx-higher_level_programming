#!/usr/bin/python3
"""JSON format file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """function writes an object to file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
