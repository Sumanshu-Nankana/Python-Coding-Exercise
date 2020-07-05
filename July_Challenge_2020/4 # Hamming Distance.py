# The Hamming distance between two integers is the number of positions at 
# which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


# ===========================================================================
# Accepted in Leetcode

class Solution(object):
    
    def getBinary(self, num):
        out = []
        res = ''
        while num!=0:
            rem = num%2
            num = num//2
            out.insert(0, str(rem))
        res = ''.join(out)
        if len(res)!=32:
            res = res.zfill(32)
        return res
    
    def hammingDistance(self, x, y):
        bin_x = self.getBinary(x)
        bin_y = self.getBinary(y)
        
        count=0
        for i in range(32):
            if bin_x[i]!=bin_y[i]:
                count+=1
        
        return count
    
obj = Solution()
x = int(input())
y = int(input())
print(obj.hammingDistance(x, y))

# ==========================================================================
# Accepted in Leetcode
# Another approach 
# Take the OR of both numbers
# and then get the binary of output
# and then count number of 1's

class Solution(object):    
    def getBinary(self, num):
        out = []
        res = ''
        while num!=0:
            rem = num%2
            num = num//2
            out.insert(0, str(rem))
        res = ''.join(out)
        return res
    
    def hammingDistance(self, x, y):
        result = x ^ y
        count = 0
        out = self.getBinary(result)
        return out.count('1')
        
obj = Solution()
x = int(input())
y = int(input())
print(obj.hammingDistance(x, y))

# ======================================================================
# Accepted in Leetcode

class Solution(object):    
    def hammingDistance(self, x, y):
        result = x ^ y
        count = 0
        while result > 0:
            count+=result&1
            result>>=1
        return count

# =====================================================================

