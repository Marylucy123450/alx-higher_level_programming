#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This is the Square class.

    A square is a geometric shape with four equal sides and four equal angles.
    It is defined by its side length.

    Attributes:
    - __size (int): Private instance attribute representing size of the square

    Methods:
    - __init__(self, size): Initializes instance ofSquare class with given size
    """

    def __init__(self, size):
        """
        Initializes an instance of the Square class with a given size.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If the provided size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
