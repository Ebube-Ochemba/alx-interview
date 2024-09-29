#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """
    args:
        grid: A list of list of integers.

    returns the perimeter of the island described in grid"""
    perimeter = 0
    for idx in range(len(grid)):
        for jdx in range(len(grid[idx])):
            if grid[idx][jdx] == 1:
                perimeter += 4
                if idx > 0 and grid[idx - 1][jdx] == 1:
                    perimeter -= 2
                if jdx > 0 and grid[idx][jdx - 1] == 1:
                    perimeter -= 2
    return perimeter
