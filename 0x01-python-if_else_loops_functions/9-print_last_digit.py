#!/usr/bin/python3
def print_last_digit(number):
    strnumber = str(number)
    last = strnumber[-1]
    print("{}".format(int(last)), end="")
    return last
