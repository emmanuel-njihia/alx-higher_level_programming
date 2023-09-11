#!/usr/bin/python3
"""Defines an subclass."""


class MyList(list):
    """Refers to class is a subclass of list class."""

    def print_sorted(self):
        """prints a sorted list in ascending order."""
        print(sorted(self))
