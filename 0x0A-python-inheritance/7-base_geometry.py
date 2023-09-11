#!/usr/bin/python3
"""A class wih a function that raises an exception"""


class BaseGeometry:
    """A class wih a function that raises an exception"""
    def area(self):
        """Raisesa an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed to it"""
        if not isinstance(value, int)
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
