#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Squuare class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String rpresentation for square"""
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, width))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values fo the attributes"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    def to_dictionary(self):
        """Return dict of a square"""
        id = self.id
        s = self.width
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': s, 'y': y}
