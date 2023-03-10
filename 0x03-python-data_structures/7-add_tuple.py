#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = check_tuple(tuple_a)
    new_tuple_b = check_tuple(tuple_b)
    return (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])


def check_tuple(tuple=()):
    if len(tuple) == 0:
        return (0, 0)
    elif len(tuple) == 1:
        return (tuple[0], 0)
    else:
        return tuple
