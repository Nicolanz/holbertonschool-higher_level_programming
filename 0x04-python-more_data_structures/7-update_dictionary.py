#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if(i == key):
            a_dictionary[i] = value
    a_dictionary.setdefault(key, value)
    return (a_dictionary)
