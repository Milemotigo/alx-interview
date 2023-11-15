#!/usr/bin/python3
'''0. Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''
    Do not return anything. The matrix must be edite
    in-place.
    '''
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(n):
            matrix[i].reverse()
