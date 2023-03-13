#!/usr/bin/python3
replace_in_list = __import__("2-replace_in_list").replace_in_list

og_list = [1, 2, 3, 4, 5]
print("Working with list: {}".format(og_list))

idx = 4
el = 9
new_list = replace_in_list(og_list, idx, el)

print("Working with list: {}".format(og_list))
print("New list: {}".format(new_list))
