#!/usr/bin/python3
"""module that refers to a class MyInt that inherits from int."""


class MyInt(int):
    """Custom class that inverts == and != operators."""

    def __eq__(self, value):
        """Override == operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator."""
        return self.real == value
