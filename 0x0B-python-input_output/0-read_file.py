#!/usr/bin/python3
"""Reads a file and writes it to stdout"""


def read_file(filename=""):
    """Reads afile and prin ts it"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
