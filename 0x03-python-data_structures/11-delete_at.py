#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 and idx > len(my_list) - 1:
        new_list = my_list
    else:
        del my_list[idx]
        new_list = my_list
    return new_list
