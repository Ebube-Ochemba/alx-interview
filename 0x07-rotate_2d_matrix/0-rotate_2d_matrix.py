#!/usr/bin/python3
"""0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list[list]): 2D int matrix
    Returns: None
    """
    # Reverse the order of the rows
    matrix.reverse()

    # Swap the elements in the diagonal only once
    for idx in range(len(matrix)):
        for j in range(idx):
            # Python idiom for swapping values without a temporary variable.
            matrix[idx][j], matrix[j][idx] = matrix[j][idx], matrix[idx][j]


"""
illustration
------------
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
--------------------
STEPS:
--------------------
1. matrix.reverse():
matrix = [[7, 8, 9],
          [4, 5, 6],
          [1, 2, 3]]
--------------------
2. "nested loop"
idx=1, j=0:
    matrix = [[7, 4, 9],
              [8, 5, 6],
              [1, 2, 3]]
idx=2, j=0:
    matrix = [[7, 4, 9],
              [8, 5, 6],
              [1, 2, 3]]
idx=2, j=1:
    matrix = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]
"""
