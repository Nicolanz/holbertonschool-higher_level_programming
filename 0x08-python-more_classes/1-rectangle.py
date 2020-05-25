#!/usr/bin/python3
"""Module to define a rectangle with
height and width specified"""


class Rectangle:
    """Class the built the rectangle"""
    def __init__(self, width=0, height=0):
        """Function to Initialize the atributtes

        Keyword Arguments:
            width {int} -- [width of the Ractangle] (default: {0})
            height {int} -- [Height of the Rectangle] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the Rectangle

        Returns:
            [int] -- [Return width to the modify it]
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Function to modify width

        Arguments:
            value {[int]} -- [New value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle

        Returns:
            [int] -- [New value]
        """
        return self.__width

    @height.setter
    def height(self, value):
        """Funtion to modify the value

        Arguments:
            value {[int]} -- [New value]

        Raises:
            TypeError: [Catchs value errors]
            TypeError: [Catchs type errors]
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
