#!/usr/bin/python3
"""This defines a function  file-reading."""


def read_file(filename=""):
    """function thatr eads text file (UTF8)then prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
