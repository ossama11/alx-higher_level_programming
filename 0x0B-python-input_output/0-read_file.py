#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): the name of the file to read from
    """
    with open(filename, "r", encoding="utf-8") as f:
        
        for line in f:
            print(line, end="")
