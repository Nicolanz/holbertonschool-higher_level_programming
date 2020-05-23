#!/usr/bin/python3
"""
Function to print a
square of a given size
"""


def print_square(size):
    """Prints the square

    Arguments:
        size {[int]} -- [Size of function]

    Raises:
        TypeError: [Catchs type errors]
        ValueError: [Catchs value errors]
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
