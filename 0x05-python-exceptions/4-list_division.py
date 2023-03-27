#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for idx in range(0, list_length):
            try:
                my_list.append(my_list_1[idx] / my_list_2[idx])
            except ZeroDivisionError:
                print("division by 0")
                my_list.append(0)
                pass
            except IndexError:
                print("out of range")
                my_list.append(0)
                pass
            except (TypeError, ValueError):
                print("wrong type")
                my_list.append(0)
                pass
    finally:
        return my_list
