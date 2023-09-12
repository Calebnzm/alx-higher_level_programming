#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns a dictionary description of the object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object with serializables.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
