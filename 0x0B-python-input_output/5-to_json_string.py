#!/usr/bin/python3
import json
"""Return json repr of an object"""


def to_json_string(my_obj):
    """Parses from json to string

    Arguments:
        my_obj {[object]} -- [object to parse]

    Returns:
        [type] -- [string]
    """
    return json.dumps(my_obj)
