#!/usr/bin/python3
""" represents class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function that represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes  new Rectangle.
        Args:
            width: The width.
            height: The height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
