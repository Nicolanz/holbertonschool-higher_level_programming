#!/usr/bin/python3
"""This is a module which contains a function
to divide two elements of a matrix. It
has it's own file .txt to tests possible
errors. It is inside te ./test file and is
called 2-matrix_divided.txt"""


def matrix_divided(matrix, div):
    """Function to divide two elements of a matrix

    Arguments:
        matrix {[list]} -- [Matrix of lists to divide]
        div {[int]} -- [Number two divide]

    Raises:
        TypeError: [Catchs type errors]
        ZeroDivisionError: [Catchs num/0 error]
        TypeError: [Catcs type errors]
        TypeError: [Catchs type errors]

    Returns:
        [list] -- [List of the elements]
    """
    newMatrix = []
    i = 0
    b = i - 1

    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if (i > 0):
            if len(matrix[i]) != len(matrix[b]):
                raise TypeError("Each row of the matrix \
must have the same size")
        b = b + 1
        new = matrix[i].copy()
        for j in range(len(matrix[i])):
            if (type(matrix[i][j]) != int and type(matrix[i][j]) != float):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            new[j] = new[j] / div
            new[j] = round(new[j], 2)
        newMatrix += [new]
    return newMatrix
