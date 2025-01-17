#!/bin/python3
# https://www.hackerrank.com/challenges/between-two-sets/problem
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# Second Method
from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

def find_lcm(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result

def find_gcd(arr):
    result = arr[0]
    for num in arr[1:]:
        result = gcd(result, num)
    return result

def count_multiples(lcm_a, gcd_b):
    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    return count


def getTotalX(a, b):
    # Step 1: Find LCM of A
    lcm_a = find_lcm(a)

    # Step 2: Find GCD of B
    gcd_b = find_gcd(b)

    # Step 3: Count valid numbers
    return count_multiples(lcm_a, gcd_b)

# First Method - Brute Force
def getTotalX(a, b):
    # Write your code here
    start = max(a)
    end = min(b)
    count = 0

    for x in range(start, end + 1):
        if all(x % i == 0 for i in a):
            if all(j % x == 0 for j in b):
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
