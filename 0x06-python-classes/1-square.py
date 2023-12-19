#!/usr/bin/python3
"""make a class Square"""

class Square:
    """properties of square."""
    def __init__(self, size):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
