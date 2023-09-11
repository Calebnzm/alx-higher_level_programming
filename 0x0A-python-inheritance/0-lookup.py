#!/usr/bin/python3
"""This module return the attributes available to an inheriting class"""


def lookup(obj):
    """This function returns a classes attributes"""
    return dir(obj)
