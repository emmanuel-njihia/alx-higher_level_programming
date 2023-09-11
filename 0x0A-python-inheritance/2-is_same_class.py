#!/usr/bin/python3
"""
Defines a function if an argument is a exactly an instance.
"""


def is_same_class(obj, a_class):
    """function that Check if an object is an instance of a class.
    Args:
        obj :The object
        a_class : The class.
    Return:
        If object is exactly an instance of a_class - True.
        if nnot return - False.
    """
    if type(obj) == a_class:
        return True
    return False
