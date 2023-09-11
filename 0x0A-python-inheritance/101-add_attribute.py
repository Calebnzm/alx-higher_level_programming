#!/usr/bin/python3
"""Adds an attribute to an object"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute (str): The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    Returns:
        None: This function modifies the object in place.
    """
    # Check if the object has the '__dict__' attribute (most custom objects do)
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
