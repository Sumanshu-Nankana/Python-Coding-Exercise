#!/bin/python3
# https://www.hackerrank.com/challenges/the-hurdle-race

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    number_of_doses = 0
    for h in height:
        if k < h:
            number_of_doses += h - k
            k = h
    return number_of_doses

# Method-2
def hurdleRace1(k, height):
    return max(0, max(height) - k)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Example input
    k = 53
    height = [
        86, 4, 83, 20, 6, 81, 58, 59, 53, 2, 54, 62, 25, 35, 79, 64, 27, 49, 32, 95, 100, 20, 58, 39, 92,
        30, 67, 89, 58, 81, 100, 66, 73, 29, 75, 81, 70, 55, 18, 28, 7, 35, 98, 52, 30, 11, 69, 48, 84,
        54, 13, 14, 15, 86, 34, 82, 92, 26, 8, 53, 62, 57, 50, 31, 61, 85, 88, 5, 80, 64, 90, 52, 47, 43,
        40, 93, 69, 70, 16, 43, 7, 25, 99, 12, 63, 99, 71, 76, 55, 17, 90, 43, 27, 20, 42, 84, 39, 96, 75, 1
    ]

    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # k = int(first_multiple_input[1])
    #
    # height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
