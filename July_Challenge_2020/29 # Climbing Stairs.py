# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
#     1 <= n <= 45

# ======================================================================
# Not accepted in Leetcode
# Recursion
# 21 / 45 test cases passed.
# Time limit exceeded for n = 44

class Solution(object):
    def fib(self,n): 
        if n <= 2: 
            return n 
        return self.fib(n-1) + self.fib(n-2) 

    def climbStairs(self, n):
        return self.fib(n)

# ====================================================================

# Accepted in Leetcode
# Approach - Solution will be sum of previous 2 values

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return n
        x = 1
        y = 2
        for i in range(3, n):
            tmp = y
            y = y + x
            x = tmp
        return x+y

# =======================================================================