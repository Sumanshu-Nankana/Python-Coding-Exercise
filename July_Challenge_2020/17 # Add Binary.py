# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

 

# Constraints:

#     Each string consists only of '0' or '1' characters.
#     1 <= a.length, b.length <= 10^4
#     Each string is either "0" or doesn't contain any leading zero.

# =======================================================================

# Accepted in Leetcode

class Solution(object):
    
    def getInteger(self, string):
        string_length = len(string)
        rev_string = string[::-1]
        i = 0
        out = 0
        while i < string_length:
            out = out + (int(rev_string[i])*(pow(2,i)))
            i+=1
        return out
    
    def getBinary(self, integer):
        out = ''
        while integer!=1:
            rem = integer%2
            integer = integer//2
            out = out + str(rem)
        out = out + str(integer)
        return out[::-1]

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a!=0:
            int1 = self.getInteger(a)
        else:
            int1 = 0
        if b!=0:
            int2 = self.getInteger(b)
        else:
            int2 = 0
        _sum = int1 + int2
        if _sum!=0:
            result = self.getBinary(_sum)
        else:
            result = '0'
        return result

# ===============================================================

# Accepted in Leetcode
# Direct add Binary Numbers
# If sum is 2 then ; carry = 1 and number = 0
# if sum is >2 then; carry = 1 and number = 1
# if sum is <=1 ;then; carry = 0 and number = 1

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rev_a = a[::-1]
        rev_b = b[::-1]
        
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))
        
        rev_a = a[::-1]
        rev_b = b[::-1]
        
        out = ''
        carry = 0
        
        i = 0
        while i < len(rev_a):
            temp = int(rev_a[i]) + int(rev_b[i]) + carry
            if temp <= 1:
                out = out + str(temp)
                carry = 0
            elif temp == 2:
                out = out + '0'
                carry = 1
            else:
                out = out + '1'
                carry = 1
            i+=1
        
        if carry == 1:
            out = out + str(carry)
        return out[::-1]

obj = Solution()
a = input()
b = input()
obj.addBinary(a, b)

# =========================================================

# Accepted in Leetcode
# Approach-3 - Slight change in approach-2

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))
        
        out = ''
        carry = 0
        
        i = len(a)-1
        while i >= 0:
            temp = int(a[i]) + int(b[i]) + carry
            if temp <= 1:
                out = out + str(temp)
                carry = 0
            elif temp == 2:
                out = out + '0'
                carry = 1
            else:
                out = out + '1'
                carry = 1
            i-=1
        
        if carry == 1:
            out = out + str(carry)
        return out[::-1]

# =====================================================================
