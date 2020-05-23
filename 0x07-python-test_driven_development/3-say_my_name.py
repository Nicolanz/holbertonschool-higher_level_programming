#!/usr/bin/python3
"""This module
is created to print
a name with first and
last name passed. It has
its own test .txt file
"""


def say_my_name(first_name, last_name=""):
    """Function to print a name

    Arguments:
        first_name {[str]} -- [First name]

    Keyword Arguments:
        last_name {str} -- [last name] (default: {""})

    Raises:
        TypeError: [If first name is not a str]
        TypeError: [If second name is not a str]
    """
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) != str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
