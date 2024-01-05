#!/usr/bin/python3
"""defines a class LockedClass"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """creates new instances of Locked Class."""

        self.first_name = "first_name"
