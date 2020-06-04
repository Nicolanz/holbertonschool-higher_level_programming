#!/usr/bin/python3
import json
"""Return json repr of an object"""


def to_json_string(my_obj):
    """Converts to json string

    Arguments:
        my_obj {[class]} -- [object]

    Returns:
        [type] -- [class]
    """
    return json.dumps(my_obj, sort_keys=True)
