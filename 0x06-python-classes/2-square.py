#!/usr/bin/python3
""" Adds a new attribute and catchs somes errors"""


class Square:
    """Class for the object"""
    def __init__(self, size=0):
        """
        Initializes Size and cacth errors
        Keyword Arguments:
            size {int} -- [Variable to store] (default: {0})
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
