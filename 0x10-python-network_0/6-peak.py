#!/usr/bin/python3
"""Module: 6-peak.py"""


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers
    """

    # Check if the list is empty
    if not list_of_integers:
        return None  # If the list is empty, return None

    # Initialize pointers for binary search
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search until low becomes equal to high
    while low < high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Compare the middle element with its adjacent element to determine the
        # search direction
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the middle element is greater than right neighbor, search left
            high = mid
        else:
            low = mid + 1  # Otherwise, search right

    # Return the peak element found at index low
    return list_of_integers[low]


# Test cases
if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))      # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))   # Output: 3
    print(find_peak([2, 2, 2]))            # Output: 2
    print(find_peak([]))                   # Output: None
    print(find_peak([-2, -4, 2, 1]))       # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4


# The complexity of the provided algorithm is O(log(n)).
# This is because the algorithm uses a binary search approach to narrow down
# the search space in each iteration. In each step, the size of the search
# space is halved, leading to a time complexity of O(log(n)).
