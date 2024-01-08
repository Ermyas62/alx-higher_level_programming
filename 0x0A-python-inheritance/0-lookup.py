#!/usr/bin/python3
""" Defines an object attributes lookup function."""

def lookup(obj):
    """Return a list of an object's availible attributes."""
    return (dir(obj))
