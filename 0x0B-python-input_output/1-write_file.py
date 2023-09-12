#!/usr/bin/python3
"""Writes to afile"""


def write_file(filename="", text=""):
    """WRItes to a file and returns no of characters writen"""
    with open(file, mode='w', encoding='utf-8') as file:
        return file.write(text)
