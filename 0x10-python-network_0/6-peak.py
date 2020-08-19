#!/usr/bin/python3
"""Module which contain a function to find
a Peak in a list"""


def find_peak(list_of_integers):
    """function to find a Peak in a lis

    Args:
        list_of_integers ([list]): [List to evaluate]
    """

    try:
        max = list_of_integers[0]
    except:
        max = None

    for i in list_of_integers:
        if i > max:
            max = i

    return(max)
