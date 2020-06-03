#!/usr/bin/python3
"""Module which creates an inherited class of list"""


class MyList(list):
    """Class to Initialize the class

    Arguments:
        list {[list]} -- [list]
    """
    def print_sorted(self):
        """Prints lists sorted"""
        lista = self.copy()
        lista.sort()
        print(lista)
