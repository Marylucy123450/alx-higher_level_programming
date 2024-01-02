#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of
a specified class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return type(obj) is a_class
