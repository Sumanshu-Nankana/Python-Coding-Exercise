# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases 
# holds:

#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital, like "Google".

# Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:

# Input: "USA"
# Output: True

# Example 2:

# Input: "FlaG"
# Output: False

# Note: The input will be a non-empty word consisting of uppercase and lowercase 
# latin letters.

# =========================================================================
# Accepted in Leetcode

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        len_ = len(word)
        for ch in word:
            if ord(ch) >=65 and ord(ch) <=90:
                count+=1
        
        if count == len_:
            return True
        if count == 0:
            return True
        if count == 1 and (ord(word[0]) >= 65 and ord(word[0]) <=90):
            return True
        
        return False

# ==========================================================================

# Accepted in Leetcode
# Another Approach
# We have only below posisble conditions
# AB...(if first two upper then from 3 to rest all should be upper)
# Ab...(if either first or 2nd is not upper - then from 2nd to last all should be lower)

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2: return True
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower(): return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper(): return False
        
        return True

# ============================================================================