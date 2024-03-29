#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest, TestCase):
    """Unit test for max_integer """

    def test_positive(self):
        """test positive values """
        self.assertEqual(max_integer([50, 100, 25]), 100)

    def test_negative(self):
        """test negative values """
        self.assertEqual(max_integer([-50, -100, -25]), -25)

    def test_mix(self):
        """test mix values """
        self.assertEqual(max_integer([50, -100, 25]), 50)

    def test_empty_list(self):
        """test empty list """
        self.assertEqual(max_integer([]), None)

    def test_dictionary(self):
        """ test dictionary """
        self.assertRaises(KeyError, max_integer, {5: 'a', 4: 'b', 3: 'c'})

    def test_one(self):
        """ test one element in list """
        self.assertEqual(max_integer([5]), 5)

    def test_string(self):
        """ test string """
        self.assertEqual(max_integer('hello'), 'o')
