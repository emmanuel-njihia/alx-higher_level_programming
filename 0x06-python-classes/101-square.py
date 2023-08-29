#!/usr/bin/python3
"""Declares a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
            Args:
                size: size of square
                position: tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the area of the square
            Return:
                Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters
            Prints an empty line if the size of the square is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Return a string representation of the square"""
        if self.__size == 0:
            return ""

        output = ""
        for i in range(self.__position[1]):
            output += "\n"

        for i in range(self.__size):
            output += " " * self.__position[0]
            output += "#" * self.__size
            output += "\n"

        return output[:-1]
