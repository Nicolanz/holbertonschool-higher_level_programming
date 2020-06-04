#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """My function

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        [bool]: [True of false if the instance inherits directly
                or indirectly the specific class]
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
