# Given a non-empty array of digits representing a non-negative integer, 
# plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# ============================================================
# Accepted in Leetcode - But Not Optimized

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        _str = ''.join(digits)
        _int = int(_str) + 1
        out = list(str(_int))
        for i in range(len(out)):
            out[i] = int(out[i])
        return out
    
obj = Solution()
digits = [1, 2, 3]
print(obj.plusOne(digits))

# =============================================================

# Accepted in Leetcode - and Better than above solution

class Solution(object):
    def plusOne(self, digits):
        temp = digits[-1] + 1
        digits[-1] = temp
        if digits[-1] < 10: return digits
        else:
            i = len(digits)-1
            flag = False
            while i>=0:
                if flag:
                    digits[i] = digits[i] + carry
                    flag = False
                if digits[i] >= 10:
                    num = digits[i]
                    digits[i] = num%10
                    carry = num//10
                    flag = True
                i-=1
            
            if flag:
                digits.insert(0, carry)
                return digits
            else:
                return digits

obj = Solution()
digits = [1,2,3]
print(obj.plusOne(digits))

# =================================================================

# Accepted in Leetcode

class Solution(object):
    def plusOne(self, digits):
        i = len(digits)-1
        while i>=0:
            if digits[i]==9:
                digits[i]=0
            elif digits[i]<9:
                digits[i]+=1
                return digits
            i-=1
        
        if digits[0]==0:
            digits.insert(0, 1)
            return digits

# ===============================================================