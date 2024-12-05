#!/usr/bin/python3
"""
Module for calculating the perimeter of an island represented in a grid.

The module provides a function to compute the perimeter of an island
where water is represented by 0 and land is represented by 1.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a given grid.

    Args:
        grid (List[List[int]]): A 2D grid where 0 represents water
        and 1 represents land.

    Returns:
        int: The total perimeter of the island.

    Raises:
        ValueError: If the input grid is empty or contains invalid values.
        TypeError: If the input is not a list of lists.
    """

    if not grid or not isinstance(grid, list):
        raise TypeError("Input must be a non-empty 2D list")

    if not all(isinstance(row, list) for row in grid):
        raise TypeError("Grid must be a list of lists")

    if not grid[0]:
        raise ValueError("Grid cannot contain empty rows")

    width = len(grid[0])
    height = len(grid)

    if any(len(row) != width for row in grid):
        raise ValueError("All rows must have the same length")

    if not all(all(cell in (0, 1) for cell in row) for row in grid):
        raise ValueError("Grid must contain only 0 and 1")

    perimeter = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
