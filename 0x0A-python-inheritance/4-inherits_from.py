#!/usr/bin/python3
"""Checks if an object is a class that inherits from another"""


def inherits_from(obj, a_class):
    """Checks if an object is a class that inheritts from another"""
    return isinstance(obj, a_class) and type(obj) is not a_class
