#!/bin/python3

# https://www.hackerrank.com/challenges/countingsort2/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):

    max_val = max(arr)
    count = [0] * (max_val+1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for index, freq in enumerate(count):
        sorted_arr.extend([index] * freq)

    return sorted_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
