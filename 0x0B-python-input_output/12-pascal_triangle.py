#!/usr/bin/python3
"""module contains the function pascal_triangle and helper function factorial
"""


def factorial(n):
    """returns the factorial of a number n
    """

    if n == 0:
        return 1
    return n * factorial(n - 1)


def pascal_triangle(n):
    """returns a list of lists. Each list being a row in the pascal triangle.
    the algo uses the pascal triangle's formula nCr=n!/((n-r)!*r!)
    time complexity O(N^2)
    """

    pascal = []

    for i in range(n):
        row = []
        for r in range(i + 1):
            row.append(factorial(i) // (factorial(i - r) * factorial(r)))
        pascal.append(row)

    return pascal
