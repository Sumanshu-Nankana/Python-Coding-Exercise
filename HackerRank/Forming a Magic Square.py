#!/bin/python3

# https://www.hackerrank.com/challenges/magic-square-forming/problem

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

possible_magic_squares = [
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

def formingMagicSquare(s):
    # Write your code here
    min_cost = float("inf")
    for magic in possible_magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])

        min_cost = min(min_cost, cost)

    return min_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
