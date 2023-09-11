#!/usr/bin/python3
"""this modules refers  function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.
    Args:
        obj (any): The object.
        att (str): attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
