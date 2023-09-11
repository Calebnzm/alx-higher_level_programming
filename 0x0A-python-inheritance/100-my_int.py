#!/usr/bin/python3

"""Rebel int"""


class MyInt(int):
    """
    A custom integer class that inherits from the built-in `int` class.

    This class inverts the behavior of the `==` and `!=` operators.

    Attributes:
        This class inherits all attributes of the built-in `int` class.

    Methods:
        __eq__(self, other): Custom operator that inverts the behavior of `==`.
        __ne__(self, other): Custom operator that inverts the behavior of `!=`.
    """

    def __eq__(self, other):
        """
        Custom equality operator that inverts the behavior of `==`.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        # Invert the equality operator
        return super().__eq__(other)

    def __ne__(self, other):
        """
        Custom inequality operator that inverts the behavior of `!=`.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        # Invert the inequality operator
        return not super().__eq__(other)
