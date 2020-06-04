#!/usr/bin/python3
"""This is the module that return an object repr"""
import json


def from_json_string(my_str):
    """Convert from string to json

    Arguments:
        my_str {[str]} -- [string]

    Returns:
        [type] -- [object]
    """
    return json.loads(my_str)
