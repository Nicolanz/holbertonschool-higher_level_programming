#!/usr/bin/python3
"""Module to create a class"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raises Expection with specified message

        Raises:
            Exception: [Exception error]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates ints

        Arguments:
            name {[str]} -- [Name]
            value {[int]} -- [Ints]

        Raises:
            TypeError: [Type Errors]
            ValueError: [Value Errors]
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
