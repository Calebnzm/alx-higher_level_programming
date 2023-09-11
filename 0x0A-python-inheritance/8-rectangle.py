#!/usr/bin/python3
"""Module defines a rectangle object"""


class BaseGeometry:
    """A class wih a function that raises an exception"""
    def area(self):
        """Raisesa an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed to it"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class rectangle that inherits from basegeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
