# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# =====================================================================================

# n = 12
# Squares less than 12 = (1,4,9) ==> So output should contain either 1 or 4 or 9 or 
# all or any pairs
# Lets suppose if output contains 1 -- then remaining number is 11
# Lets suppose if output contains 2 -- then remaining number is 8
# Lets suppose if output contains 9 -- then remaining number is 3
                            
# Now We need to check all Sqaures less than 11 = (1,4,9)
# Now We need to check all Sqaures less than 8 = (1,4)
# Now We need to check all Sqaures less than 3 = (1)

# Now, 11 can be make using 1,4,9, lets take 1 by 1
# Similarly 8 can be made using 1, 4
# Similarly 3 can be made using 1

# Now take sqaures less than 10 = (1,4,9)
# Squares less than 7 = (1,4)
# and so on..
#                                           12
        
#                             11            8              3
        
#                     10      7    2   | 7      4  |     2
            
#                  9   6  1 |6  3 |1   |6  3  |3  0 |   1
                
#                 and so on.....
                
# So this is recursive approach..But we see like for 7 (we caclulate two times)
# For 6 ,we calculated 3 times - So overlapping sub-problems

# So at end - we will check we reach '0' in which least(minimum) steps is our answer
# So for 12 it's '3' (12-8 , 8-4, 4-4 ==> 4+4+4 )  3 steps

# So better to use dynamic programming approach

# Take a array - and save the number of least sqaures to form that number....
# So that we can use that - instead of re-calculating it

# ==================================================================================

# Recursive approach
# But Not Accepted in Leetcode ==> Time Limit Exceeded for input = 42   (41/588 test cases passed)

class Solution(object):
    def numSquares(self, n):
        return self.helper(n)
    
    def helper(self, n):
        # Base-cases
        if n == 0: return 0
        if n < 0: return 9999999
        
        min_ = n   # Max n squares possible (with 1) for worst answer
        for i in range(1, n+1):
            min_ = min(self.helper(n-i*i), min_)
        
        return min_+1
        
obj = Solution()
n = int(input())
print(obj.numSquares(n))

# =======================================================================================

# Dynamic Programming - Memoization

# We will create a array to store earlier solved problems
# and array will be 1 large than size of 'n' as we will store value if 0
# [0,1,2,3,4,5,6,7,8,9,10,11,12] ==> So total 13 index - all will be initialize with 0

# Still not accepted in Leetcode ==> Time Limit Exceeded for input 7168  (502 / 588 test cases passed)

import sys
class Solution(object):
    def numSquares(self, n):
        self.dp = [0]*(n+1)
        return self.helper(n, self.dp)
    
    def helper(self, n, dp):
        # Base-cases
        if n == 0: return 0
        if n < 0: return 9999999
        if self.dp[n] > 0: return self.dp[n]
        
        min_ = n   # Max n squares possible (with 1) for worst answer
        for i in range(1, n+1):
            min_ = min(self.helper(n-i*i, self.dp), min_)
        
        self.dp[n] = min_+1
        return min_+1
        
obj = Solution()
n = int(input())
sys.setrecursionlimit(10000)  # Without setting this, even here as well code is failing with Recursion Limit
print(obj.numSquares(n))

# ========================================================================================

# Dynamic Programming - Memoization

# 588 / 588 test cases passed.
# But looks its Still not optimized  its taking more than 7000 seconds


class Solution(object):
    def numSquares(self, n):
        self.dp = [0]*(n+1)
        return self.helper(n, self.dp)
    
    def helper(self, n, dp):
        # Base-cases
        if n == 0: return 0
        if self.dp[n] > 0: return self.dp[n]
        
        min_ = n   # Max n squares possible (with 1) for worst answer
        
        # we improved a little bit - instead of running till n
        # we run till sqaures < n
        i = 1
        while i*i <= n:
            min_ = min(self.helper(n-i*i, self.dp), min_)
            i+=1
        
        self.dp[n] = min_+1
        return min_+1
        
obj = Solution()
n = int(input())
print(obj.numSquares(n))

# =====================================================================================

# Accepted in Leetcode
# and take 3000 ms (more optimized)

class Solution(object):
    def numSquares(self, n):
        dp = [0]*(n+1)
        for i in range(1, n+1):
            min_ = i   # for all 1's worst case
            y, sq = 1, 1
            while sq <= i:
                min_ = min(min_, 1+dp[i-sq])
                y+=1
                sq = y*y
            dp[i] = min_
        return dp[n]

# ======================================================================================