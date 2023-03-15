#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []

    for i in sorted(list(set_1)):
        for j in sorted(list(set_2)):
            if i is j:
                common_list.append(i)

    return set(common_list)
