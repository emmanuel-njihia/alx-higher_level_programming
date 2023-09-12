#!/usr/bin/python3
"""class Student."""


class Student:
    """represents a student."""

    def __init__(self, first_name, last_name, age):
        """initializes a new Student.
        Args:
            first_name (str): the student first name.
            last_name (str):the student last name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns  dictionary representation of the Student class."""
        return self.__dict__
