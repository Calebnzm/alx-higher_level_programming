#!/usr/bin/python3
"""Unittests for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        # Test when the list contains positive integers
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_mixed_numbers(self):
        # Test when the list contains mixed positive and negative integers
        result = max_integer([1, 3, 4, -2])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        # Test when the list contains negative integers
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)

    def test_empty_list(self):
        # Test when the list is empty
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        # Test when the list contains a single element
        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()
