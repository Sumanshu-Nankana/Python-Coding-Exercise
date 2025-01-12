#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize the highest and lowest scores with the first game
    highest_score = scores[0]
    lowest_score = scores[0]
    count_break_best_record = 0
    count_break_worst_record = 0

    for i in range(1, len(scores)):
        # Check if the current score breaks the highest record
        if scores[i] > highest_score:
            count_break_best_record += 1
            highest_score = scores[i]
        # Check if the current score breaks the lowest record
        elif scores[i] < lowest_score:
            count_break_worst_record += 1
            lowest_score = scores[i]

    # Return the counts as a list
    return [count_break_best_record, count_break_worst_record]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
