#!/usr/bin/python3
"""Module of the class
"""


class Student:
    """My class
    """
    def __init__(self, first_name, last_name, age):
        """Constructor

        Arguments:
            first_name {[str]} -- [First name]
            last_name {[str} -- [Last name]
            age {[int]} -- [Age]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dict repr of Student

        Returns:
            [dict] -- [Dictionary]
        """
        return self.__dict__
