#!/bin/usr/python3
"""This module contains a function to return a
list of available attributes and methods of an object"""


def lookup(obj):
    """Function

    Arguments:
        obj {[Any Type]} -- [Object]

    Returns:
        [list] -- [List of available attributes and methods of an object"]
    """
    return dir(obj)
