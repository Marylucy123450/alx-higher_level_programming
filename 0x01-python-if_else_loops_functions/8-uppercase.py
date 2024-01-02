#!/usr/bin/python3

# Define the `uppercase` function that takes a string as an
# argument
def uppercase(str):
    """Print a string in uppercase."""

    # Iterate through each character in the input string
    for c in str:
        # Check if the character is a lowercase letter by
        # comparing its ASCII value
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert the lowercase character to uppercase by
            # subtracting 32 from its ASCII value
            c = chr(ord(c) - 32)

        # Print the character without a newline (using "end=")
        print("{}".format(c), end="")

    # Print a newline to separate the output from the next line
    print("")
