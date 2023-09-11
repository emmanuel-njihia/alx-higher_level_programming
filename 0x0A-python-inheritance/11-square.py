#!/usr/bin/python3
"""This module defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that represents a square."""

    def __init__(self, size):
        """initialize new square.
        Args:
            size:size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
