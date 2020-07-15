# Given an input string, reverse the string word by word.
# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a 
# single space in the reversed string.

# Note:
#     A word is defined as a sequence of non-space characters.

#     Input string may contain leading or trailing spaces. However, 
#     your reversed string should not contain leading or trailing spaces.

#     You need to reduce multiple spaces between two words to a single space in the 
#     reversed string.

# Follow up:
# For C programmers, try to solve it in-place in O(1) extra space.

# ================================================================
# Accepted in Leetcode
# Here we are using extra array, But in quetion it asked to do in O(1)

class Solution(object):
    def reverseWords(self, s):
        if len(s) == 0: return ""
        if len(s) == 1: return s.strip()
        temp = s.split()
        end = len(temp) - 1
        start = 0
        while start <= end:
            temp[start],temp[end] = temp[end].strip(), temp[start].strip()
            start+=1
            end-=1           
        return ' '.join(temp)

# ==================================================================

# Accepted in Leetcode
# wihout any extra space

class Solution(object):
    def reverseWords(self, s):
        result, i, n = "", 0, len(s)
        while i < n:
            while i < n and s[i] == " ": 
                i += 1
            if i >= n: 
                break
            j = i + 1
            while j < n and s[j] != " ":
                j += 1
            sub = s[i:j]
            if len(result) == 0: 
                result = sub
            else:
                result = sub + " " + result
            i = j + 1
        return result 

# =========================================================================