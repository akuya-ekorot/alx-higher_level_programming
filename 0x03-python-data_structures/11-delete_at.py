#!/usr/bin/python
def delete_at(my_list=[], idx=0):
    my_list[:] = my_list
    if not (idx >= len(my_list) or idx < 0):
        my_list[:] = my_list[:idx] + my_list[idx + 1:]

    return my_list
