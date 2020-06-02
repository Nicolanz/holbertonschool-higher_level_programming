#!/usr/bin/python3
"""Module which contains a function to
know if the object is an instance of, or if
the object is an instance of a class that inherited from,
the specified class"""


def is_kind_of_class(obj, a_class):
    """Function

    Arguments:
        obj {[Any type]} -- [object]
        a_class {[class]} -- [class]

    Returns:
        [boolean] -- [True or false]
    """
    return isinstance(obj, a_class)
