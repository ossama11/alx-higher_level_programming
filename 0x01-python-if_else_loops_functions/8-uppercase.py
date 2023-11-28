#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char_upper = ord(str[i]) - 32
        print("{}".format(chr(char_upper)), end="")
print()
