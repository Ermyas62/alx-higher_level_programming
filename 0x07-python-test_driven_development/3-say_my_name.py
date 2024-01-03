#!/usr/bin/python3

"""
this is the "3-say_my_name" module.
the 3-say_my_name module supplies on efunction, say_my_name.
"""

def say_my_name(first_name, last_name=""):
    """
    prints "my name is" followed by the first name and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
