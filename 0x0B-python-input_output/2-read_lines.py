#!/usr/bin/python3
"""Module to read lines depending on the user"""


def read_lines(filename="", nb_lines=0):
    """Print the number of lines of a file

    Keyword Arguments:
        filename {str} -- [Name of the file] (default: {""})
        nb_lines {int} -- [Number of lines to print] (default: {0})
    """
    def numberOfLines(filename):
        """Function to know te num of lines

        Arguments:
            filename {[str]} -- [Name of the file]

        Returns:
            [int] -- [Number of lines]
        """
        with open(filename) as f:
            lines = 0
            for i in f.readlines():
                lines += 1
        return lines

    with open(filename, mode='r', encoding="UTF8") as fobj:
        str = ""
        if nb_lines <= 0 or nb_lines >= numberOfLines(filename):
            str = fobj.read()
        else:
            for i in range(nb_lines):
                str += fobj.readline()
    print(str, end="")
