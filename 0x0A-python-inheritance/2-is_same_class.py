#!/usr/bin/python3
"""Module which contains a funtion
to know if an object is exactly
an instance of the specific class"""


def is_same_class(obj, a_class):
    """Function.

    Arguments:
        obj {[Any type]} -- [Object of the class]
        a_class {[class]} -- [class]

    Returns:
        [boolean] -- [True or false]
    """
    if obj.__class__ is a_class:
        return True
    else:
        return False
