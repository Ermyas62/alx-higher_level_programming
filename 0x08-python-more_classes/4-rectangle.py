#!/usr/bin/python3
"""
Module 4-rectangle
Defines a rectangle class.
"""

class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """ Intialize a rectangle instance.
        Args:
           width: width of the rectangle
           height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ returns an informal and nicely printable string representation
            of a reectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]
    
    def __repr__(self):
        """Return a string representation of a rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle ({}, {}".format(self.__width, self.__height)

    @property
    def width(self):
        """ retrives the width of a rectangle instance. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width of a rectangle instance
        Args:
            value: value of the width must be a postive number
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrives the height of a rectangle instance. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of a rectangle instance
        Args:
            value: value of the height must be a postive number
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle instance
          returns:
                area of the rectangle, given by height * width
        """
        return self.__width * self.height

    def perimeter(self):
        """ calculates the perimeter of a rectangle instance
           returns:
                  perimeter of the rectangle, given by
                           2 * (height + width)
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)


