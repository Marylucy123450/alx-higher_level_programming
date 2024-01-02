#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of, or
inherited from, a specified class."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
