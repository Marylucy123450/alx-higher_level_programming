#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -2, -3]), -1)

    def test_duplicate_max(self):
        """Test max_integer with duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_single_element(self):
        """Test max_integer with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_mixed_numbers(self):
        """Test max_integer with a list containing mixed numbers"""
        self.assertEqual(max_integer([1, 2, -3, 0, 5, -6, 10]), 10)

    def test_float_numbers(self):
        """Test max_integer with a list containing floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.1]), 4.1)

if __name__ == '__main__':
    unittest.main()
