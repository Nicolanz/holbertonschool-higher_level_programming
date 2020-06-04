#!/usr/bin/python3
"""Loads 0bject from file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”

    Arguments:
        filename {[str]} -- [Name of the file]

    Returns:
        [type] -- [object]
    """
    with open(filename, mode='r') as f:
        myObj = json.load(f)
    return myObj
