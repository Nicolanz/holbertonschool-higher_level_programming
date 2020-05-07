#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    b = 0
    for i in matrix:
        new = matrix[b].copy()
        for j in range(len(new)):
            new[j] = new[j] * new[j]
        new_matrix += [new]
        b = b+1
    return(new_matrix)
