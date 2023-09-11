"""This module return the attributes available to an inheriting class"""
#!/usr/bin/python3

def lookup(obj):
    """This function returns a classes attributes"""
    return dir(obj)
