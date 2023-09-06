#!/usr/bin/python3
"""
This script defines a function that adds two integer.
"""


def add_integer(a, b=98):
    """
    This function returns the sum of integer  of a and b.

    If either a or b is a not an integer orfloat, TypeError is raised.
    """

    # Check if a is non-integer or non- float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is non integer or a non- float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Casting a and b to integers and return their addition
    return int(a) + int(b)
