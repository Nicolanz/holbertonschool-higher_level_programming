#!/usr/bin/python3
"""1-square - Crates a class with private attribute size"""


class Square:
    """Class Square"""
    def __init__(self, size):
        """method is run as soon as an object of a class is instantiated

        Arguments:
            size {[int]} -- Private variable
        """
        self.__size = size
