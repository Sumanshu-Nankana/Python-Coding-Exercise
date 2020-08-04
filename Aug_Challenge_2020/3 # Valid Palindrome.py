# Given a string, determine if it is a palindrome, considering only 
# alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

# Constraints:

#     s consists only of printable ASCII characters.

# =====================================================================

# Accepted in Leetcode

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1: return True
        start = 0
        end = len(s)-1
        while start < end:
            while(start < end and not s[start].isalnum()): 
                start+=1
            while(start < end and not s[end].isalnum()):
                end-=1
            if start < end and s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True

# ======================================================================
