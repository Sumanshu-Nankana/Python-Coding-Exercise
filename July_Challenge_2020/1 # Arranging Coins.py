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

# ==================================================================================
# Accepted in Leetcode
# More optimized in O(logn) way
# Approach - we know Sum of first n number is n*(n+1)/2
# or if we can se sum of first K stairs is K*(k+1)/2
# And this value should be <= N
# and we need to find the max value of 'K'
class Solution(object):
    def arrangeCoins(self, n):
        start = 0
        end = n
        while start <= end:
            mid = start + (end-start)//2
            k = mid
            if n >= int(k*(k+1)/2):
                start = mid+1
            else:
                end = mid-1
        return start-1
    
obj = Solution()
n = int(input())             # number of coins
print(obj.arrangeCoins(n))

# ==================================================================================
# Accepted in Leetcode
# More Optmized in O(1)
# Approach:
# k*(k+1)/2 <= N
# k^2 + K <= 2N
# k^2 + K - 2N = 0
# K = sqrt(2N+1/4)-1/2
import math
class Solution(object):
    def arrangeCoins(self, n):
        return int(math.sqrt(2*n+0.25) - 0.5)

    
obj = Solution()
n = int(input())             # number of coins
print(obj.arrangeCoins(n))

# ==================================================================================