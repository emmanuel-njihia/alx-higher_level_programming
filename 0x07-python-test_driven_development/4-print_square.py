#!/usr/bin/python3
"""
This function prints a square using the # character.
"""


def print_square(size):
    """
    function to print a square with the # character.

    Args:
        size (int): The height/width.

    Raises:
        TypeError: If size is non-integer.
        ValueError: If size is < 0
    """

    # Check if size is integer and < 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
