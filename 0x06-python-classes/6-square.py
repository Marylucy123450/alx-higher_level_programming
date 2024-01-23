#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Represents a square geometry.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new instance of
        the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character '#'.

    Properties:
        size (int): Gets or sets the size of the square.
        position (tuple): Gets or sets the position of the square.

    Raises:
        TypeError: If size is not an integer or if position is not a tuple of
        2 positive integers.
        ValueError: If size is less than 0 or if position contains
        non-positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).
        Raises:
            TypeError: If size is not an integer or if position is not a tuple
            of 2 positive integers.
            ValueError: If size is less than 0 or if position contains
            non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
