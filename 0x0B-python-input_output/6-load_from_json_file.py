#!/usr/bin/python3
"""
contains the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """creates an object from a "JSON filr" """
    with open(filename, 'r', encoding="utf-8") as file:
        create_obj = json.load(file)
        return create_obj
