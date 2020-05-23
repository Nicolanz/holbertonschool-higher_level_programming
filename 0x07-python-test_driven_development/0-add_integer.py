#!/usr/bin/python3
"""Module which contains a function to
sum two ints or floats. It contains it's
own .txt file to test possible errors.
it is inside the ./test folder and is called
0-add_integer.txt"""


def add_integer(a, b=98):
    """Function to add two ints

    Arguments:
        a {[int]} -- [First parameter]

    Keyword Arguments:
        b {int} -- [Second parameter] (default: {98})

    Raises:
        TypeError: [Raises Tpye Errors for a]
        TypeError: [Raises Type Errors for b]

    Returns:
        [int] -- [Returns the sum for a and b]
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
