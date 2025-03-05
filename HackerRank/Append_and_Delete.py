#!/bin/python3
# https://www.hackerrank.com/challenges/append-and-delete/problem

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):

    # Find common matching string length
    common_length = 0
    for se, te in zip(s, t):
        if se == te:
            common_length += 1
        else:
            break

    # Calculate required operations
    deletions = len(s) - common_length
    insertions = len(t) - common_length
    total_operations_required = deletions + insertions

    if k == total_operations_required:
        return "Yes"
    elif k > total_operations_required:
        if (k - total_operations_required) % 2 == 0 or k >= len(s) + len(t):
            return "Yes"
        else:
            return "No"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
