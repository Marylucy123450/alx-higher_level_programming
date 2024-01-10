#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the original list
    for element in my_list:
        if element == search:
            # Replace the element if it matches the search element
            new_list.append(replace)
        else:
            # Keep the element as is if it doesn't match the search element
            new_list.append(element)

    return new_list
