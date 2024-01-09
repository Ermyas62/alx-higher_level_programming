#!/usr/bin/python3
"""
The "class_to_json" function container
"""


def class_to_json(obj):
    """ retruns the dictionary description with simple data structure
    (list, dictionary, string, integer and booleean)
    for JSON serialization of an object"""
    return obj.__dict__
