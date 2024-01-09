#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        first_char = sentence[0]  # Get the first character
    else:
        first_char = None  # Set to None if the sentence is empty

    length = len(sentence)  # Calculate the length of the sentence

    return length, first_char  # Return a tuple with length and first character
