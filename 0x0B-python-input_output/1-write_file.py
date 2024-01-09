#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): the name of the file to write to
        text (str): the string to write to the file

    Returns:
        int: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
