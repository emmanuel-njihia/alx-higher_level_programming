#!/usr/bin/python3
"""This function converts  string-to-JSON."""
import json


def to_json_string(my_obj):
    """This converts to JSON from a string object."""
    return json.dumps(my_obj)
