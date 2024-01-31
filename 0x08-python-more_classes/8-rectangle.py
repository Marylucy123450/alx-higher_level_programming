#!/usr/bin/python3
"""
This module defines the Rectangle class with width, height,
number_of_instances, symbol attributes,
and a static method bigger_or_equal.
"""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        number_of_instances (int): The number of instances of Rectangle.
        symbol: The symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes a rectangle
        with a given width and height.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation that can be
        used to recreate the object.
        __del__(self): Prints a message when an instance of Rectangle
        is deleted.
        Static method bigger_or_equal(rect_1, rect_2): Returns the
        biggest rectangle based on the area.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    number_of_instances = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value, "height")
        self.__height = value

    def validate_dimension(self, value, dimension):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(dimension))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(dimension))

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height) \
            if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = [str(self.symbol) * self.__width for _ in range(self.__height)]
        result = '\n'.join(lines)
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
