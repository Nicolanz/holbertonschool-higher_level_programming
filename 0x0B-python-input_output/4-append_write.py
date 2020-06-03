#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Writes a string to a text file
    and creates it if it does not exist.
    It appends new content

    Keyword Arguments:
        filename {str} -- [Name of the file] (default: {""})
        text {str} -- [Text] (default: {""})

    Returns:
        [type] -- [Num of cars]
    """
    chars = 0
    with open(filename, "a", encoding="utf8") as f:
        for i in text:
            f.write(i)
            chars += 1
    return chars
