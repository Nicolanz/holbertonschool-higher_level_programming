#!/usr/bin/python3
"""
  Module to create a new rectangle
"""
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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of rectangle

        Returns:
            [int] -- [Area]
        """
        return self.__width * self.__height

    def __str__(self):
        """String

        Returns:
            [str] -- [string]
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
