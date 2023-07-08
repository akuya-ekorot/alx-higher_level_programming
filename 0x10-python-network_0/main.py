#!/usr/bin/python3
""" test the function find_peak """

import unittest
find_peak = __import__('6-peak').find_peak


class TestFindPeak(unittest.TestCase):
    """ Class to test the function find_peak """

    def test_empty_list(self):
        """ Test with empty list """
        self.assertEqual(find_peak([]), None)

    def test_one_element(self):
        """ Test with one element """
        self.assertEqual(find_peak([1]), 1)

    def test_two_elements(self):
        """ Test with two elements """
        self.assertEqual(find_peak([1, 2]), 2)
        self.assertEqual(find_peak([2, 1]), 2)

    def test_general_lists(self):
        """ Test with five elements """
        self.assertEqual(find_peak([1, 2, 4, 6, 3]), 6)
        self.assertEqual(find_peak([4, 2, 1, 2, 3, 1]), 3)
        self.assertEqual(find_peak([4, 2, 1, 2, 2, 2, 3, 1]), 4)


if __name__ == "__main__":
    unittest.main()
