#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Attempt to perform division
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            # Handle wrong type
            print("wrong type")
            division_result = 0
        except IndexError:
            # Handle out of range
            print("out of range")
            division_result = 0
        finally:
            # Append the result to the result list
            result.append(division_result)

    return result
