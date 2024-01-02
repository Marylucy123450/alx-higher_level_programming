#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
