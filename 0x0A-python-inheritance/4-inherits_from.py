#!/usr/bin/python3
"""This module refers to  an inherited class-checking function."""


def inherits_from(obj, a_class):
    """function that checks if an object
    is an inherited instance of a class.
    Args:
        obj: This ithe object to check.
        a_class: The class .
    Return:
        If obj is an inherited instance of a_class - True.
        if not then return- False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
