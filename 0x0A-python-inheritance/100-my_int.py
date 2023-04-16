#!/usr/bin/python3
"""module contains class MyInt"""


class MyInt(int):
    """rebel sibling of int, they're not equals"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
