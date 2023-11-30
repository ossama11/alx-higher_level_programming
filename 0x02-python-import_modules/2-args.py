#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    plural = "" if num_args == 1 else "s"

    print(f"{num_args} argument{plural}:")
    if num_args > 0:
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
else:
    exit()
