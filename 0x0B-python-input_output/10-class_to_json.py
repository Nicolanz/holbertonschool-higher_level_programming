#!/usr/bin/python3
"""Module that  returns the dictionary description with simple
data structure(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""
import json


def class_to_json(obj):
    """My Function

    Arguments:
        obj {[type]} -- [Object]

    Returns:
        [type] -- [object Parsed]
    """
    objeto = json.dumps(obj.__dict__)
    c = json.loads(objeto)
    return c
