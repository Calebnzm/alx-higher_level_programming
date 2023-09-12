#!/usr/bin/python3
"""Seraches afile and appennds after a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """Searches and updates a file"""
    updated_lines = []

    with open(filename, 'r') as file:
        for line in file:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
