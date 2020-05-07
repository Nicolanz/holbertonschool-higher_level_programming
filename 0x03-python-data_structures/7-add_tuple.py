#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if(len(tuple_a) == 0):
        tupleUnoA = 0
        tupleUnoB = 0
    if(len(tuple_b) == 0):
        tupleDosA = 0
        tupleDosB = 0
    if(len(tuple_a) == 1):
        tupleUnoA = tuple_a[0]
        tupleUnoB = 0
    if(len(tuple_b) == 1):
        tupleDosA = tuple_b[0]
        tupleDosB = 0
    if(len(tuple_a) >= 2):
        tupleUnoA = tuple_a[0]
        tupleUnoB = tuple_a[1]
    if(len(tuple_b) >= 2):
        tupleDosA = tuple_b[0]
        tupleDosB = tuple_b[1]
    a = tupleUnoA + tupleDosA
    b = tupleUnoB + tupleDosB
    tupp = (a, b)
    return (tupp)
