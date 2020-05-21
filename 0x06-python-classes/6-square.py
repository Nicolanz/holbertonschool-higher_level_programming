#!/usr/bin/python3
"""Module to create a class for an object and modify
private attributes size and position.
There are also two methods to get the area for
size and print the square"""


class Square:
    """Class of the object"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns size to then modify it

        Returns:
            [int] -- [Returns size]
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Function to assign new size value
        Arguments:
            value {[int]} -- [Value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns position to then modify it

        Returns:
            [tuple] -- [Returns position]
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Function to assign new position value
        Arguments:
            value {[tuple]} -- [Value]

        Raises:
            TypeError: [Catchs type errors]
        """
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Finds the current square
        Returns:
            [int] -- [Returns the area]
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the Square
        """
        if self.__size <= 0:
            print()
        else:
            if (self.__position[1] > 0):
                for j in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for c in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()
