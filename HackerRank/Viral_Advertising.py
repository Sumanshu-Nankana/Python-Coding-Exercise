#!/bin/python3
# https://www.hackerrank.com/challenges/strange-advertising/problem

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    recipients =  5
    total_likes = 0
    for _ in range(n):
        liked = recipients // 2
        total_likes = total_likes + liked
        recipients = liked * 3
    return total_likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
