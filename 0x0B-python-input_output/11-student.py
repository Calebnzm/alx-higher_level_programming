#!/usr/bin/python3
""" that replaces all attributes of the Student instance:"""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and ge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        a = attrs
        return {key: value for key, value in self.__dict__.items() if key in a}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (dict): A dict containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
