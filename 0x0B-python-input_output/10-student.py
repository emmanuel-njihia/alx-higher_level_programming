#!/usr/bin/python3
""" class Student."""


class Student:
    """ student class."""

    def __init__(self, first_name, last_name, age):
        """initialize a new Student.
        Args:
            first_name (str):the student first name.
            last_name (str): the student last name.
            age (int): the student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function gets a dictionary representation of the Student.
        If attrs is a list of strings, it represents only those attributes
        included in the list.
        Args:
            attrs (list):the attributes.
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__
