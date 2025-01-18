#!/bin/python3
# https://www.hackerrank.com/challenges/picking-numbers/problem

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    frequency = defaultdict(int)
    for i in a:
        frequency[i] += 1

    max_length = 0
    for key, value in frequency.items():
        max_length = max(max_length, frequency[key] + frequency.get(key - 1, 0))

    return max_length


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
