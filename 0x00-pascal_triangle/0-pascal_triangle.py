#!/usr/bin/python3
"""0-pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal triangle of n"""

    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(1, n):
        new_row = [1]
        for col in range(1, row):
            new_row.append(triangle[row - 1][col] +
                              triangle[row - 1][col - 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
