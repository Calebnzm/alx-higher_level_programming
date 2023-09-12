#!/usr/bin/python3
"""If attrs is a list, only attribute names contained are retrieved."""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs: A list of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        a = attrs
        return {key: value for key, value in self.__dict__.items() if key in a}
