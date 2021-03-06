#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    and creates it if it does not exist.
    It also overwrites the text to the file.

    Keyword Arguments:
        filename {str} -- [Name of the file] (default: {""})
        text {str} -- [Text] (default: {""})

    Returns:
        [int] -- [Number of characters written]
    """
    chars = 0
    with open(filename, "w", encoding="utf8") as f:
        for i in text:
            f.write(i)
            chars += 1
    return chars
