#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    """Reads files

    Keyword Arguments:
        filename {str} -- [Name of the file] (default: {""})
    """
    with open(filename, encoding='utf8') as f:
        read = f.read()
    print(read)
