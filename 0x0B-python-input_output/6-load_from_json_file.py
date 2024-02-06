#!/usr/bin/python3
"""Defines a function for loading an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename (str): The name of the file containing the
         JSON representation.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
