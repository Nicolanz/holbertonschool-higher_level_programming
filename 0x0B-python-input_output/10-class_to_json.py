#!/usr/bin/python3
"""Module that  returns the dictionary description with simple
data structure(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """Funtion of the mosule

    Arguments:
        obj {[type]} -- [Object]

    Returns:
        [type] -- [data repr of the obj]
    """
    return obj.__dict__
