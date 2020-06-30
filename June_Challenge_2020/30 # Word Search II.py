# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.

# Example:

# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]


# Note:
#     All inputs are consist of lowercase letters a-z.
#     The values of words are distinct.
#===================================================================================
# Accepted in Leetcode
# For explanation check - https://www.youtube.com/watch?v=3PT9QjgYTQc
# 

class Trie(object):
    def __init__(self):
        self.endOfWorld = False
        self.children = [None]*26
        
    def insert(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Trie()
            curr = curr.children[idx]
        
        curr.endOfWorld = True    
    
class Solution(object):
    def dfs(self, i, j, trie, s):
        c = self.board[i][j]
        if c=='$': return
        self.board[i][j] = '$'
        t = trie.children[ord(c)-ord('a')]
        if t is not None:
            ss = s + c
            if t.endOfWorld:
                self.result.add(ss)
            
            if i < len(self.board)-1:
                self.dfs(i+1, j, t, ss)
            if j < len(self.board[0])-1:
                self.dfs(i, j+1, t, ss)
            if i > 0:
                self.dfs(i-1, j, t, ss)
            if j > 0:
                self.dfs(i, j-1, t, ss)
        
        self.board[i][j] = c              
            
    def findWords(self, board, words):
        if len(words)==0: return []
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        result = set()
        self.board = board
        self.result = result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie, "")
        
        result_v = list(result)
        return result_v

# ===================================================================================
