#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    my_dict = a_dictionary.copy()
    for i in my_dict:
        if i == key:
            a_dictionary.pop(key)
    return (a_dictionary)
