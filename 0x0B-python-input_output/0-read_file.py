#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read. Default is empty

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
