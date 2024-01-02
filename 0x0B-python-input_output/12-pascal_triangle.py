#!/usr/bin/python3
"""Defines a function that Generate Pascal's triangle up to n rows."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        row = [1]  # The first element of each row is always 1

        # Generate the middle elements of the row
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])

        row.append(1)  # The last element of each row is always 1

        triangle.append(row)

    return triangle


# Example usage
if __name__ == "__main__":
    # Test with n = 5
    result = pascal_triangle(5)
    for row in result:
        print("[{}]".format(",".join(map(str, row))))
