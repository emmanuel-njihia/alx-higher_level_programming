#!/usr/bin/python3
"""Defines a class and an inherited class."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance or
    inherited instance of a class.

    Args:
        obj: The object.
        a_class: The class.

    Returns:
        If obj is an instance or inherited instance of a_class - True.
        if not then return - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
