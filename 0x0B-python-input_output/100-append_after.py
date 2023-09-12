#!/usr/bin/python3
"""text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts text after each line
    containing a given string in a file.
    Args:
        filename (str): the name of the file.
        search_string (str): the string to search.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as k:
        for line in k:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
