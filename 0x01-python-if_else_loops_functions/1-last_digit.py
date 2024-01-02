#!/usr/bin/python3
import random

# Generate a random integer between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Calculate the last digit (always positive) using the modulo operator
digit = abs(number) % 10

# If the original number is negative, make the last digit negative as well
if number < 0:
    digit = -digit

# Print the message with the last digit information
print(f"Last digit of {number:d} is {digit:d} and is ", end="")

# Check the value of the last digit and print the appropriate message
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
