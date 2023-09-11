#!/usr/bin/python3
"""This refers to a class Rectangle that is inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle."""

    def __init__(self, width, height):
        """This intializes new Rectangle.
        Args:
            width : the width.
            height : The height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def __str__(self):
        """This return the print() and str() rctangle representation."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
