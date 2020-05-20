#!/usr/bin/python3
"""Adds a new attribute and has a new public method"""


class Square:
    """Class of the object"""
    def __init__(self, size=0):
        """
        Initializes Size and catchs error
        Keyword Arguments:
            size {int} -- [Attribute] (default: {0})

        Raises:
            TypeError: [Cacths type errors]
            ValueError: [Catchs value errors]
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Finds the current square area
        Returns:
            [int] -- [Returns the area]
        """
        return self.__size * self.__size
