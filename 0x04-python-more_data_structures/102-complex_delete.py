#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deletees = []
    for key, s_value in a_dictionary.items():
        if s_value == value:
            deletees.append(key)
    for key in deletees:
        del a_dictionary[key]
    return a_dictionary
