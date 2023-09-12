#!/usr/bin/python3
"""Python class-to-JSON function."""


def class_to_json(obj):
    """
    function that returns
    dictionary description of a simple data structure.
    """
    return obj.__dict__
