#!/usr/bin/python3
def convert(str):
    word = ""
    for i in str:
        word += i
    return word


def remove_char_at(str, n):
    string = list(str)
    if (len(str) > n and n >= 0):
        string[n] = ''
    string = convert(string)
    return string
