#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []

    for int in my_list:
        if int % 2:
            list_result.append(False)
        else:
            list_result.append(True)

    return list_result
