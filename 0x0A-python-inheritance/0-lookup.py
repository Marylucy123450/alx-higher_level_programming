#!/usr/bin/python3
"""This module provides a single function, lookup(obj), which returns a list
containing the names of all attributes and methods of the given object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
    obj: The object for which to retrieve attributes and methods.

    Returns:
        A list of strings representing the attributes and
          methods of the object.
    """
    return dir(obj)
