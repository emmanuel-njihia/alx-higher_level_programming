#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Represent the rectangle class.

    Attributes:
        number_of_instances (int): The Rectangle instances' numbers.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The new rectangle width.
            height (int): The new rectangle height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the Rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the Rectangle printable presentation.

        Represents the rectangle with the # .
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for k in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if k != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return the Rectangle string representation."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """Print a message for every rectangle deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
