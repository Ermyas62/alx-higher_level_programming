#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance of class.
    Args:
         obj (any): The object to check.
         a_class (Type): The class to match the type of obj to.
    Returns:
          if obj is an instance of class - True.
          otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
