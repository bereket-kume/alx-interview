#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """
    function to calculate perimeter
    return perimeter of grid
    """
    row = len(grid)
    column = len(grid[0])
    count = 0

    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    count += 1

                if (row - i) == 1 or grid[i + 1][j] == 0:
                    count += 1

                if j == 0 or grid[i][j - 1] == 0:
                    count += 1

                if (column - j) == 1 or grid[i][j + 1] == 0:
                    count += 1

    return count
