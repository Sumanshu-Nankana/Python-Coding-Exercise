# You have a total of n coins that you want to form in a staircase shape, 
# where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:
# n = 5

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# Because the 3rd row is incomplete, we return 2.

# Example 2:

# n = 8

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.

# ===============================================================================
# NOT ACCEPTED IN LEETCODE
# We Get MEMORY error with FOR LOOP for larger inputs example - 1804289383
# because we are using range() function - which create a list in a memory first
class Solution(object):
    def arrangeCoins(self, n):
        if n==0: return 0
        for i in range(1, n+1):
            n = n - i
            if n < 0: return i-1
            if n == 0: return i

obj = Solution()
n = int(input())             # number of coins
print(obj.arrangeCoins(n))

# =======================================================================================

# Accepted in Leetcode
# With for loop, we are not getting any memory Error
class Solution(object):
    def arrangeCoins(self, n):
        if n==0: return 0
        i = 1
        while n > 0:
            n = n - i
            i = i + 1
        if n < 0: return i-2
        if n == 0: return i-1
    
obj = Solution()
n = int(input())             # number of coins
print(obj.arrangeCoins(n))

# ===================================================================================