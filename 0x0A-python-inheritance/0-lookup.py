#!/usr/bin/python3
"""
This script defines a function
that returns a list of available
attributes
"""


def lookup(obj):
    """
    function returns list of available attributes .
    """

    return dir(obj)
