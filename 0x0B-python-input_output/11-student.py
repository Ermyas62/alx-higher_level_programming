#!/usr/bin/python3
"""
 Module for class student
"""


class Student:
    """
        A class student that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): last name of student.
            age (int): age of student
        Methods:
            __init__ - intializes the studen instance.
            to_json - retrives dictionary repr of student instance.
    """
    def __init__(self, first_name, last_name, age):
        """intializes the students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """returns a dictionary representation of a student instance
        Args:
            attr (list): attribute names that are to be retrived"""

        if type(attr) is list and all([type(x) == str for x in attr]):
            return {k: v for k, v in self.__dict__.items() if k in attr}
        else:
            return self.__dict__.copy()
