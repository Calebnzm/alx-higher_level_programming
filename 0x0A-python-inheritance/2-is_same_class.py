#!/usr/bin/python3
"""This module checks if an object is a specific class"""


def is_same_class(obj, a_class):
    """This function checks if an object is a specific class

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """

    return type(obj) == a_class
