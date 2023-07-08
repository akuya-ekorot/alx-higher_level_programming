#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """

    li = list_of_integers

    if len(li) == 0:
        return None

    # A peak is not necessarily the highest number in the list
    # It is the number that is greater than or equal to its neighbors

    # If the list has only one element, that element is the peak
    if len(li) == 1:
        return li[0]

    # If the list has two elements, the greater one is the peak
    if len(li) == 2:
        return max(li)

    # If the list has more than two elements
    # The peak is the middle element if it is greater than or equal to
    # its neighbors
    # Otherwise, the peak is found recursively in the left or right half
    # of the list depending on whether the left or right neighbor is greater
    # than the middle element
    middle = len(li) // 2
    if li[middle] > li[middle - 1] and li[middle] > li[middle + 1]:
        return li[middle]

    if li[middle] <= li[middle - 1]:
        return find_peak(li[:middle])

    if li[middle] <= li[middle + 1]:
        return find_peak(li[middle + 1:])

    return None
