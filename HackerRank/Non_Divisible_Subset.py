#!/bin/python3
# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):

    # find the frequency array of remainder_counts
    remainder_counts = [0]*k
    for num in s:
        index = num % k
        remainder_counts[index] += 1

    # start with at most one remainder with remainder 0
    result = min(remainder_counts[0], 1)

    # iterate over remainder pairs, we will run only half
    for i in range(1, (k//2) +1):
        if i != k - i:   # 4!=4
            result += max(remainder_counts[i], remainder_counts[k - i])
        else:
            result += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
