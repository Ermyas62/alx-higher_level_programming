#!/usr/bin/python3
"""defines a class-checking function."""


def inherits_from(obj, a_class):
    """check if an object is exactly an instance of given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match thr type of obj to.
    Returns:
          if obj is exactly an instance of a_class - True.
          otherwise - False'
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
