'''This is a module that defines an addition function'''
#!/usr/bin/python3

def add_integer(a, b=98):
    '''
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
