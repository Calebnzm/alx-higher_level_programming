#!/usr/bin/python3

"""Module defines a rectangle object"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
