#!/usr/bin/python3
"""Module for 2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Parameters:
        matrix (list[list[int]]): the 2D matrix to be rotated.

    Returns:
        None
    """
    # Reverse the order of the rows
    matrix.reverse()

    # Swap the elements in the diagonal only once
    for idx in range(len(matrix)):
        for j in range(idx):
            # Python idiom for swapping values without a temporary variable.
            matrix[idx][j], matrix[j][idx] = matrix[j][idx], matrix[idx][j]
