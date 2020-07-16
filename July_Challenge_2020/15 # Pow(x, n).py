# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000

# Example 2:

# Input: 2.10000, 3
# Output: 9.26100

# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Note:

#     -100.0 < x < 100.0
#     n is a 32-bit signed integer, within the range [−231, 231 − 1]

# ====================================================================
# Accepted in Leetcode
# But we are not allowed to use inbuilt power function
class Solution(object):
    def myPow(self, x, n):
        return pow(x, n)

obj = Solution()
x = float(input())
n = int(input())
print(obj.myPow(x, n))

# ======================================================================

# Not Accepted

# 291 / 304 test cases passed.
# Time Limit Exceeded for x = 0.00001 and n = 2147483647

class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
        i = 1
        res = 1
        while i <= abs(n):
            res = res * x
            i += 1
        return res

obj = Solution()
x = float(input())
n = int(input())
print(obj.myPow(x, n))

# =========================================================================
# Accepted in Leetcode

class Solution(object):
    def myPow(self, x, n):
        if n<0:
            return 1/self.power(x, -n)
        else:
            return self.power(x, n)
    
    def power(self, x , n):
        if n == 0:
            return 1
        
        temp = self.power(x, n//2)
        
        if n%2==0:
            return temp*temp
        else:
            return x*temp*temp
# =======================================================================