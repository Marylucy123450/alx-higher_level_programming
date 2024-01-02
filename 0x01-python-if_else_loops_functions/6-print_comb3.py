#!/usr/bin/python3

# Loop through tens place values from 0 to 9
for tens in range(0, 10):
    # Loop through ones place values from the current tens place value to 9
    for ones in range(tens + 1, 10):
        # Check if the tens place is 8 and the ones place is 9
        if tens == 8 and ones == 9:
            # If it is, print the combination without a comma and space
            print("{}{}".format(tens, ones))
        else:
            # For all other combinations, print with a comma and space
            print("{}{}".format(tens, ones), end=", ")
