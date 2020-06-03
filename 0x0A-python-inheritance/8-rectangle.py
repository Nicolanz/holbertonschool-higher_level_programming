#!/usr/bin/python3
"""Module to create a new rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class

    Arguments:
        BaseGeometry {[class]} -- [SuperClass]
    """
    def __init__(self, width, height):
        """Constructor

        Arguments:
            width {[int]} -- [positive ints]
            height {[int]} -- [positive ints]
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
