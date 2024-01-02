#!/usr/bin/python3
"""Defines functions for writing text files in UTF-8 encoding."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
     of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
