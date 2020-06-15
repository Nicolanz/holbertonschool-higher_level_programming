#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Contructor

        Args:
            id ([type], optional): [Id]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Covert python object to json

        Args:
            list_dictionaries ([list]): [list of dicts]

        Returns:
            [str]: [json repr]
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
