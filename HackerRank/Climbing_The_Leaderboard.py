#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# Time Limit Exceeded couple of Tests Cases
""" Ranks[1    2   3   4]
    indx [0    1   2   3]
ranked = [100, 90, 80, 70]
player = [60, 65, 72, 80, 90, 105]

For the first player (60), the inner loop checks [100, 90, 80, 70]. It breaks when 60 >= 70 and assigns a rank.
For the second player (65), the inner loop checks [100, 90, 80, 70] again, breaking when 65 >= 70 and assigning a rank.
"""
def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_ranks = sorted(set(ranked), reverse=True)
    player_ranks = []

    for p_score in player:
        for rank, l_score in enumerate(unique_ranks):
            if p_score >= l_score:
                player_ranks.append(rank + 1)
                break
        else:
            player_ranks.append(len(unique_ranks) + 1)

    return player_ranks


# In this we will compare from Reverse to avoid re-check
"""
ranked = [100, 90, 80, 70]
player = [60, 65, 70, 80, 90, 100]

For the first player (60), the while loop checks [100, 90, 80, 70] starting from the last rank, moving j backwards when 60 >= 70.
For the second player (65), the while loop continues from the updated j position and again checks [100, 90, 80, 70], moving j again when 65 >= 70.
"""
def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_ranks = sorted(set(ranked), reverse=True)
    player_ranks = []
    l = len(unique_ranks)
    j = l - 1

    for p_score in player:
        while j >= 0 and p_score >= unique_ranks[j]:
            j -= 1
        player_ranks.append(j + 2)

    return player_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
