#!/usr/bin/python3
def element_at(my_list, idx):
    len_my_list = len(my_list) - 1
    if idx < 0 or idx > len_my_list:
        return (None)
    else:
        return (my_list[idx])
