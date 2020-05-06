#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    i = 0
    if (size == 0):
        letter = i
    else:
        letter = sentence[i]
    tup = (size, letter)
    return(tup)
