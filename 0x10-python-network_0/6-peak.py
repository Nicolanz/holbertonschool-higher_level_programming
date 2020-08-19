#!/usr/bin/python3
"""Module which contain a function to find
a Peak in a list"""


def find_peak(list_of_integers):
    """function to find a Peak in a lis

    Args:
        list_of_integers ([list]): [List to evaluate]
    """
    lista = sorted(list_of_integers)
    try:
        return(lista[-1])
    except:
        return(None)
