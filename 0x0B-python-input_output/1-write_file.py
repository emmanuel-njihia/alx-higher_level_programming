#!/usr/bin/python3
"""This defines a function that writes in file."""


def write_file(filename="", text=""):
    """function that  writes a string to a UTF8 text file.
    Args:
        filename : the name of the file.
        text:the text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
