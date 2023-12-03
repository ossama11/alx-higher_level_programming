#!/usr/bin/env python3
def no_c(my_string):
    i = 0
    result = ""
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            result += my_string[i]
    return (result)
