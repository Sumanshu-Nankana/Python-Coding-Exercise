#!/bin/python3

# https://www.hackerrank.com/challenges/circular-array-rotation/problem

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

"""
new_index = ( old_index + k ) % n   ==> we did mod-n so that number should be within range
But ideally query is
new_index = old_index + k

Now, we are not doing rotation, so we should know, the mapping between original_index and new_index

we need to find the element at new_index
but we are not doing any actual rotation OR modifying the array

So, we should know...which element (old_location), will come at asked location (new_location) after rotation

old_index = new_index - k
So to keep it in range we will do mod n

old_index = ( new_index - k ) % n
But, modulus take the positive numbers ..only
So,final query is:
old_index = (new_index - k + n) % n

where new_index (is asked query index ---)
old_index = (query_index - k + n ) % n
"""
def circularArrayRotation(a, k, queries):
    # Write your code here
    result = []
    for q in queries:
        old_index = (q - k + n) % n
        result.append(a[old_index])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
