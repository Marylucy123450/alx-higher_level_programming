#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    max_val = my_list[0]  # Initialize max_val with the first element

    # Iterate through the list
    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found

    return max_val  # Return the maximum value
