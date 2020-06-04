#!/usr/bin/python3
"""Writes an object to a text file using json repr"""
import json


def save_to_json_file(my_obj, filename):
    """Functions to write the object in defined repr

    Arguments:
        my_obj {[type]} -- [Any type]
        filename {[type]} -- [string]
    """
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
