#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    result = 0

    for number in my_list:
        if number not in unique_set:
            result += number
            unique_set.add(number)

    return result
