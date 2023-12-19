#!/usr/bin/python3
"""Define a Magicclass matching exactly a bytecode"""


import math


class MagicClass:
    """represent a circle."""

    def __init__(self, radius=0):
        """Initializea MagicClass.

        Arg:
            radius (float or int): the radius
        """
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def cirumference(self):
        """Return the circumfrance """
        return (2 * math.pi * self.__radius)
