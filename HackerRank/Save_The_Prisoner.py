#!/bin/python3
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

#Method-1 (Without using any Formula)
# Many Tests Failed with TLE (Time Limit Exceeded Error)
# Because m & n are very high 10^9
def saveThePrisoner(n, m, s):
    # Write your code here
    # There is minimum 1 candy, so we can give to prisoner sitting on chair s
    current = s
    # Now, assign remaining candies (m-1) - to other prisoners
    for i in range(1, m):
        current += 1
        if current > n:
            current = 1
    return current

#Method-2 (Using Formula)
# ALl Tests Passed
def saveThePrisoner(n, m, s):
    result = (s + m - 1) % n
    if result != 0:
        return result
    else:
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
