#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, row, column, obstacles):
    # Queen can move in below directions
    # Top
    # Bottom
    # Left
    # Right
    # Top-Left
    # Top-Right
    # Bottom-Left
    # Bottom-Right

    # Step1: Initialize the Maximum distance in each directions by assuming no obstacles
    directions = {
        "top": n - row,
        "bottom": row - 1,
        "left": column - 1,
        "right": n - column,
        "top-left": min(n - row, column - 1),
        "top-right": min(n - row, n - column),
        "bottom-left": min(column - 1, row - 1),
        "bottom-right": min(n - column, row - 1)
    }

    # Step2: For each obstacle, check if it lies in one of the 8 directions, and if so, update the max steps the queen can take
    for obs_row, obs_column in obstacles:
        # Obstacle in Same column
        if obs_column == column:
            if obs_row > row:
                # Obstacle in top direction
                directions["top"] = min(directions["top"], obs_row - row - 1)
            else:
                # Obstacle in bottom direction
                directions["bottom"] =  min(directions["bottom"], row - obs_row - 1)

        # Obstacle in Same Row
        elif obs_row == row:
            if obs_column > column:
                # Obstacle in right direction
                directions["right"] = min(directions["right"], obs_column - column - 1)
            else:
                # Obstacle in left direction
                directions["left"] = min(directions["left"], column - obs_column - 1)

        # Obstacle in Diagonals
        elif abs(obs_row - row) == abs(obs_column - column):
            if obs_row > row and obs_column > column:
                # Obstacle in Top-Right
                directions["top-right"] = min(directions["top-right"], obs_row - row - 1)
            elif obs_row > row and obs_column < column:
                # Obstacle in Top-Left
                directions["top-left"] = min(directions["top-left"], obs_row - row - 1)
            elif obs_row < row and obs_column < column:
                # Obstacle in Bottom-Left
                directions["bottom-left"] = min(directions["bottom-left"], row - obs_row - 1)
            elif obs_row < row and obs_column > column:
                # Obstacle in Bottom-Right
                directions["bottom-right"] = min(directions["bottom-right"], row - obs_row - 1)

    # Step3: Sum All Values of Directions.
    return sum(directions.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
