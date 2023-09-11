#!/usr/bin/python3
"""
base geometry class BaseGeometry.
"""


class BaseGeometry:
    """function that represent base geometry."""

    def area(self):
        """return anot yet implemented eexception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter.
        Args:
            name (str): The name for parameter.
            value (int): The parameter
        Raises:
            TypeError: If value is non integer.
            ValueError: If value is less than  0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
