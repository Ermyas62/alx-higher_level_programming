#!/usr/bin/python3
"""defines abase geometry class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """intialize a new rectangle.

        Args:
            width (int): The width of new rectangle.
            height *int): The height of the new rectangle.
         """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
