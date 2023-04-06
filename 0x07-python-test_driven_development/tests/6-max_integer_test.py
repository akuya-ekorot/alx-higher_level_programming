#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.max = max_integer

    def test_list_integer(self):
        with self.assertRaises(TypeError):
            self.max(["a", 3, 8])
            self.max([1.0, 3, 8])

    def test_empty_list(self):
        self.assertEqual(self.max([]), None)

    def test_max_value(self):
        self.assertEqual(self.max([1, 4, 3]), 4)
        self.assertEqual(self.max([1, -4, 3]), 3)
