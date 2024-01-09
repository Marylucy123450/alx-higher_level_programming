#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the integer is divisible by 2 (i.e., it's even)
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list
