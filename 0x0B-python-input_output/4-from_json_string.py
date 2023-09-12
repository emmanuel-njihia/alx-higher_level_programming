#!/usr/bin/python3
""" JSON-to-object function."""
import json


def from_json_string(my_str):
    """function returns  Python object from a JSON string."""
    return json.loads(my_str)
