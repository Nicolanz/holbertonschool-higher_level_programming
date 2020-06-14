#!/usr/bin/python3
"""
Module of the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle ([class]): [Parent class]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size ([int]): [size of the square class]
            x (int, optional): [x]. Defaults to 0.
            y (int, optional): [y]. Defaults to 0.
            id ([type], optional): [id]. Defaults to None.
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """Returns string to print

        Returns:
            [str]: [string to print]
        """
        return ("[Square] ({:d}) {:d}/{:d} - {}".format(
            self.id, self.x, self.y, self.size))
