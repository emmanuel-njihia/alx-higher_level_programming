#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Refers base geometry class."""

    def area(self):
        """Raise an exception stating area() is not implemented."""
        raise Exception("area() is not implemented")
