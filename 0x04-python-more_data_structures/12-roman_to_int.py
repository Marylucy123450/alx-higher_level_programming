#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is a valid string and not empty
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    # Define a dictionary to map Roman numerals to their integer values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Initialize the total value and a variable to track the previous value
    total = 0
    prev_value = 0

    # Iterate through the input string in reverse order
    for char in roman_string[::-1]:
        value = roman_numerals.get(char)
        if not value:
            return 0  # Return 0 if an invalid character is found

        # Check if the current value is greater than or equal to
        # the previous value
        if value >= prev_value:
            total += value  # Add the current value to the total
        else:
            total -= value  # Subtract the current value from the total

        prev_value = value  # Update the previous value for the next iteration

    return total  # Return the computed integer value
