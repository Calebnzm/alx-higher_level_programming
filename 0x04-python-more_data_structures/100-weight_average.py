#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    weights = 0
    for element, w in my_list:
        total += element * w
        weights += w
    return total / weights
