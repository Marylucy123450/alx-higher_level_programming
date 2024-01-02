#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class
   that inherited (directly or indirectly) from a specified class."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
