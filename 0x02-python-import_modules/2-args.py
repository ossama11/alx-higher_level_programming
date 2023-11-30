#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

len_argv = len(sys.argv)
print(f"{len_argv - 1} argument:")
for i in range(len_argv):
    if i != 0:
        print(f"{i}:", sys.argv[i])
        i = i + 1
