# Given a non-empty string s and a dictionary wordDict containing 
# a list of non-empty words, add spaces in s to construct 
# a sentence where each word is a valid dictionary word. Return all 
# such possible sentences.

# Note:

#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

# ==============================================================

# 31 / 36 test cases passed.
# Time Limit Exceeded

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
        for w in wordDict:
            len_ = len(w)
            if s[:len_] == w:
                if len(w) == len(s):
                    result.append(w)
                else:
                    tmp = self.wordBreak(s[len_:], wordDict)
                    for t in tmp:
                        result.append(w + " " + t)
        return result
    
obj = Solution()
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
obj.wordBreak(s, wordDict)

# ======================================================================

# Accepted in Leetcode

# We will solve Time Limit Problem using Dynamic Programming
# By storing the value, so that we don't need to call the same function 
# again which we already solve

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = {}
        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = word_break(s[len(w):])
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result
        return word_break(s)

obj = Solution()
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
obj.wordBreak(s, wordDict)

# ==================================================================