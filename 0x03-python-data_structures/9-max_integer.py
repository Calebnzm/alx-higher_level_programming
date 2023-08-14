#!/usr/bin/python3

def max_integer(my_list=[]):
    a = len(my_list)
    if a < 1:
        return None
    else:
        largest = 0
        for i in my_list:
            if i > largest:
                largest = i
    return largest
