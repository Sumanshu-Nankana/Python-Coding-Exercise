#!/bin/python3
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    letter_to_position = {letter: position for position, letter in enumerate(string.ascii_lowercase)}
    max_height = max(h[letter_to_position[ch]] for ch in word)
    return max_height * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()