#!/bin/python3
# https://www.hackerrank.com/challenges/bigger-is-greater/problem

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Step1: Convert String to list
    w = list(w)
    n = len(w)

    # Step2: Find the first index i from the right where w[i] < w[i+1]
    i = n - 2
    while i >=0 and w[i] >= w[i+1]:
        i -= 1

    if i == -1:
        return "no answer"

    # Step3: Find the smallest character on the right side of i that is bigger than w[i]
    j = n - 1
    while w[j] <= w[i]:
        j -= 1

    # Step4: Swap characters at i and j
    w[i], w[j] = w[j], w[i]

    # Step5: Reverse the suffix string at i+1
    w[i+1:] = reversed(w[i+1:])

    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
