#!/usr/bin/python3
"""Defines a Class that defines a student."""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance"""
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """Return string representation of a Student instance"""
        return "{} {} {}".format(self.first_name, self.last_name, self.age)
