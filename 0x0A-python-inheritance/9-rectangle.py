#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """A class representing base geometry"""
    def area(self):
        """Raises an exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle object with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
