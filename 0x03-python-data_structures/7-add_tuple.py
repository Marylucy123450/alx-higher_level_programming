#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b is smaller than 2 elements, append 0s to make them
    # both have 2 elements using the += operator.
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Extract the first two elements of each tuple (or use 0 if not available)
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Calculate the sum of the corresponding elements and create a new tuple
    result = (a1 + b1, a2 + b2)

    return result
