#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
matrix:
    if not matrix:
        return []
    else:
        return [list(map(lambda x : x**2, i))]
