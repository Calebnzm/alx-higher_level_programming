#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest = float('-inf')
    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
            l_key = key
    return l_key
