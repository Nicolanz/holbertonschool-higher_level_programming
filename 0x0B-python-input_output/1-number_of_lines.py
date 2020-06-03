#!/usr/bin/python3
"""Counts the number of lines in a file"""


def number_of_lines(filename=""):
    """function to count number of lines

    Keyword Arguments:
        filename {str} -- [Filename] (default: {""})

    Returns:
        [int] -- [number of lines]
    """
    lines = 0
    with open(filename) as f:
        for i in f.readlines():
            lines += 1
    return lines
