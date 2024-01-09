#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:

        for i in range(len(row)):
            print("{:d}".format(row[i]), end=" " if i < len(row) - 1 else "")
        print()  # Move to the next line after printing a row
