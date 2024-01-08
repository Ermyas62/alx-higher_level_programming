#!/usr/bin/python3
"""defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is exactly an instance of given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match thr type of obj to.
    Returns:
          if obj is exactly an instance of a_class - True.
          otherwise - False'
    """
    if isinstance(obj, a_class):
        return True
    return False
