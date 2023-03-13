#!/usr/bin/python3
element_at = __import__("1-element_at").element_at

my_list = [1, 2, 3, 4, 5]

print("Working with list: {}".format(my_list))

idx = 3
el = element_at(my_list, idx)
if el is None:
    print("\tFailed: Expected {:d} but got none".format(4))
else:
    print("\tPassed: Expected {:d} and got {:d}".format(4, el))

idx = -1
el = element_at(my_list, idx)
if el is None:
    print("\tPassed: Expected None and got None")
else:
    print("\tFailed: Expected None but got {:d}".format(el))

idx = 5
el = element_at(my_list, idx)
if el is None:
    print("\tPassed: Expected None and got None")
else:
    print("\tFailed: Expected None but got {:d}".format(el))


my_list = []

print("Working with list: {}".format(my_list))

idx = 3
el = element_at(my_list, idx)
if el is None:
    print("\tPassed: Expected None and got None")
else:
    print("\tFailed: Expected None but got {:d}".format(el))

idx = -1
el = element_at(my_list, idx)
if el is None:
    print("\tPassed: Expected None and got None")
else:
    print("\tFailed: Expected None but got {:d}".format(el))

idx = 5
el = element_at(my_list, idx)
if el is None:
    print("\tPassed: Expected None and got None")
else:
    print("\tFailed: Expected None but got {:d}".format(el))
