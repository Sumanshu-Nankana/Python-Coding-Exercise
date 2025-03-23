#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
def extraLongFactorials(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    print(result)


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
