#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new_str = str[:n] + str[n + 1:]
        return new_str
    else:
        return str
