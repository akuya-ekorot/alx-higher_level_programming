#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    my_sum = 0

    for i in my_list:
        if i not in uniq:
            my_sum += i
            uniq.append(i)

    return my_sum
