#!/usr/bin/python3
"""Parese a JSON"""


import json


def from_json_string(my_str):
    """Parses a JSON"""
    return json.loads(my_str)
