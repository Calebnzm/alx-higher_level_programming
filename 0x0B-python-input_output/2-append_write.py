#!/usr/bin/python3
"""Apeends characters to a file"""


def append_write(filename="", text=""):
    """Appends characters to afile"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
