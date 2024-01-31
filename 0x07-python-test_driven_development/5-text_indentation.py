#!/usr/bin/python3
"""
This module defines the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation_chars = ".?:"
    index = 0

    # Skip leading spaces
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        # Print the current character without a newline
        print(text[index], end="")

        # Check for newline or indentation characters
        if text[index] == "\n" or text[index] in indentation_chars:
            if text[index] in indentation_chars:
                # Print two new lines after encountering ., ? or :
                print("\n")

            # Skip consecutive spaces after newline or indentation characters
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue

        # Move to the next character
        index += 1
