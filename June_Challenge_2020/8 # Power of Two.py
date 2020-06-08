# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 2^0 = 1

# Example 2:

# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:

# Input: 218
# Output: false

# ========================================================
# Accepted in Leetcode

import math
class Solution(object):
    def isPowerOfTwo(self, n):
        i = 0
        out = -999999
        while(out < n):
            out = int(math.pow(2, i))
            i += 1
            if out == n:
                return True
        return False

obj = Solution()
n = int(input())
print(obj.isPowerOfTwo(n))

# ===========================================================

# Another approach
# number should be > 0 and 
# 00000000000001  = 1 (which is a power of 2)
# 00000000000010  = 2 (which is a power of 2)
# 00000000000100  = 4 (which is a power of 2)
# 00000000001000  = 8 (which is a power of 2)
# So, in binary representation, if number of ones = 1 then it's power of 2

# Another approach
# number should be > 0 and
# if we subtract 1 from given number example
# n = 8 which is 1000
# n-1 = 7 which is 0111
# AND of n & n-1 is 0
# if AND of n & n-1 is 0 ==> then it's divisible by 2

# Accepted in Leetcode 

# ====================================================

class Solution(object):
    def isPowerOfTwo(self, n):
        if n > 0 and (n & n-1) == 0:
            return True
        else:
            return False

# ====================================================



