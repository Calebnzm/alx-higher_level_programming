#!/usr/bin/python3
"""This module a class MyList that inherits from list"""


class MyList(list):
    """This class inherits from class list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
