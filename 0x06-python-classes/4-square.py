#!/usr/bin/python3
"""Module to create a class for an object and modify private attribute size"""


class Square:
    """Class of the object"""
    def __init__(self, size):
        """Instantiation of size

        Arguments:
            size {[int]} -- [Attribute]
        """
        self.__size = size

    @property
    def size(self):
        """Returns size to then modify it

        Returns:
            [int] -- [Returns size]
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Function to assign new value
        Arguments:
            value {[int]} -- [Value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Finds the current square area
        Returns:
            [int] -- [Returns the area]
        """
        return self.__size * self.__size
