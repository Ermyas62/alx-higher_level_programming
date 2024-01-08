#!/usr/bin/python3
"""class called BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this class is square that inherits from Rectangle"""

    def __int__(self, size):
        """This is the instantation.

        Args:
            size (int): the size of the new square.
        """
        self.integer_validator("size", size)
        supper().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """this function return a descriptiion about the square"""
        return ("[square] {}/{}".format(self.__size, self.__size))
