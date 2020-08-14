# Given a string which consists of lowercase or uppercase letters, 
# find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# ==============================================================================
# Accepted in Leetcode
# Approach = Palindrome can be of even length or odd length

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        result = 0
        odd_found = False
        
        for _,c in counts.items():
            if c%2==0:
                result += c
            else:
                odd_found = True
                result += c - 1
        
        if odd_found: result+=1
        return result
        
# ==============================================================================
