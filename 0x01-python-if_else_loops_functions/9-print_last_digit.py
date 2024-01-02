#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the last digit of the number using the modulo operator (%)
    last_digit = abs(number) % 10

    # Print the last digit without a newline (using "end=")
    print(last_digit, end="")

    # Return the value of the last digit
    return last_digit
