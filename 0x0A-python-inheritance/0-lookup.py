#!/usr/bin/python3
"""This module contains a function to return a
list of available attributes and methods of an object"""


def lookup(obj):
    """function to return a
    list of available attributes and methods of an object

    Arguments:
        obj {[type]} -- [object]

    Returns:
        [type] -- [list of available attributes and methods]
    """
    return dir(obj)
