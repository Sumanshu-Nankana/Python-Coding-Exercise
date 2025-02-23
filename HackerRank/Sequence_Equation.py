#!/bin/python3

# https://www.hackerrank.com/challenges/permutation-equation/problem

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

# Method-1 (using Find index using index() function of list
def permutationEquation(p):
    # Write your code here
    result = []
    for i in range(1, len(p)+1):
        index_1 = p.index(i) + 1
        index_2 = p.index(index_1) + 1
        result.append(index_2)

    return result


# Method-2 (Store Index in a dictionary for quick lookup)
def permutationEquation(p):

    result = []
    index_map = {value: index+1 for index, value in enumerate(p)}
    for i in range(1, len(p) + 1):
        index_1 = index_map[i]
        index_2 = index_map[index_1]
        result.append(index_2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
