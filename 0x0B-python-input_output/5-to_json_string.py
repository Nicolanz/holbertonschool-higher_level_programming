#!/usr/bin/python3
"""Return json repr of an object"""
import json


def to_json_string(my_obj):
    """Parses from json to string

    Arguments:
        my_obj {[Type]} -- [object to parse]

    Returns:
        [type] -- [string]
    """
    return json.dumps(my_obj)
