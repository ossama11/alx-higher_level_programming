#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for item in my_list:
        new_list.append(item)
    len_new_list = len(new_list) - 1
    if idx < 0 or idx > len_new_list:
        return (my_list)
    else:
        new_list[idx] = element
        return (new_list)
