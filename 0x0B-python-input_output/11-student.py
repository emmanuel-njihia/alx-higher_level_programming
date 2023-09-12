#!/usr/bin/python3
"""class Student."""


class Student:
    """ student representation."""

    def __init__(self, first_name, last_name, age):
        """initializes a new Student.
        Args:
            first_name (str): the student first name.
            last_name (str): the student last name.
            age (int): the student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): the attributes.
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__

    def reload_from_json(self, json):
        """function which replaces all attributes of the Student.
        Args:
            json (dict): the value pairs to replace attributes with.
        """
        for n, v in json.items():
            setattr(self, n, v)
