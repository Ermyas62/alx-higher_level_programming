#!/usr/bin/python3
"""
the "from_json_string" function container
"""

import json


def from_json_string(my_str):
    """return an object representesd by a json string"""
    return json.loads(my_str)
