# Given a non-negative integer num, repeatedly add all its digits until 
# the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# =============================================
# Accepted in Leetcode
# But in Question it has written don't use loop

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        sum_ = 0
        while num>=10:
            while num>0:
                rem = num%10
                num = num//10
                sum_ += rem
            if sum_ < 10:
                return sum_
            num = sum_
            sum_=0

obj = Solution()
num = int(input())
obj.addDigits(num)

# =======================================================

# Accepted in Leetcode

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num%9

obj = Solution()
num = int(input())
obj.addDigits(num)

# =========================================================