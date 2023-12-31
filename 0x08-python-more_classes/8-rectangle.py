#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height.
    Attributes:
        number_of_instances: number of rectangular instances,
        increments with every instantiation,
        decrements with every deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Intialize a rectangle instance.
        Args:
           width: width of the rectangle
           height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns an informal and nicely printable string representation
            of a reectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """return a string representation of a rectangile instance that is
           able to create a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ finds the biggest rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            the instance with the biggest area, or rect_1 if both
            rectangles have the ssame area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
