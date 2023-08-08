#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        result += c
    print(result)
