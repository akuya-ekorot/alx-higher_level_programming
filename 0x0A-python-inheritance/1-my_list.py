#!/usr/bin/python3
"""contains the subclass MyList that inherits from list and quicksort"""


def quicksort(list):
    """quicksort implementation to sort a list"""
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quicksort(left) + middle + quicksort(right)


class MyList(list):
    """inherits from list. has additional methods and attributes."""

    def print_sorted(self):
        """prints the list sorted in ascending order"""
        print(quicksort(self))
