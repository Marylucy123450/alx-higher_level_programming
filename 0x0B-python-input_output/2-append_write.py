#!/usr/bin/python3
"""Defines functions for appending text to files in UTF-8 encoding."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
