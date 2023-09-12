#!/usr/bin/python3
"""This defines a function tht aappends text."""


def append_write(filename="", text=""):
    """function that appends a string to the end of a UTF8 text file.
    Args:
        filename : the name of the file.
        text: The string to append.
    Return:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
