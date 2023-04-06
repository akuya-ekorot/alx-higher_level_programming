#!/usr/bin/python3
"""This module contains the function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    # check for errors in calling the function
    check_types(matrix, (int, float))
    check_size(matrix, len(matrix[0]))
    check_div(div)

    divided_matrix = []
    for array in matrix:
        divided_array = []
        for element in array:
            divided_array.append(round(element / div, 2))
        divided_matrix.append(divided_array)

    return divided_matrix


def check_div(div):
    """Checks if the div arguement passed is a float or int and not zero """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")


def check_size(matrix, size):
    """Checks if the sizes of the arrays in the matrix are equal"""
    for array in matrix:
        if len(array) != size:
            raise TypeError("Each row of the matrix must have the same size")


def check_types(matrix, types):
    """checks if the types of elements in the matrix are integers or floats"""
    for array in matrix:
        for element in array:
            if not isinstance(element, types):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
