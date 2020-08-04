# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true

# Example 2:

# Input: 5
# Output: false

# Follow up: Could you solve it without loops/recursion?

# ========================================================

# Accepted in Leetcode

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        n = num
        count = 0
        while n > 1:
            n >>= 2
            count+=2
        
        return (n << count) == num

# =====================================================

# Accepted in Leetcode

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and ((num & (num-1))==0) and (num%3==1)

# =======================================================

# Accepted in Leetcode

class Solution(object):
    def isPowerOfFour(self, num):
        if (num == 0): 
            return False
        while (num != 1): 
                if (num % 4 != 0): 
                    return False
                num = num // 4
        return True

# ============================================================