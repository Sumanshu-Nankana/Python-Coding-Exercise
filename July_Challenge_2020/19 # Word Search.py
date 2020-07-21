# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


# Constraints:
#     board and word consists only of lowercase and uppercase English letters.
#     1 <= board.length <= 200
#     1 <= board[i].length <= 200
#     1 <= word.length <= 10^3

# ============================================================
# Accepted in Leetcode

class Solution(object):
    
    def search(self, i, j, idx):
        # last character
        if idx == len(self.word)-1:
            return True
        
        self.visited[i][j] = 1
        
        if (i>0 and self.visited[i-1][j]==0 and (self.board[i-1][j]==self.word[idx+1]) 
            and self.search(i-1, j, idx+1)):
            return True
    
        if (j>0 and self.visited[i][j-1]==0 and (self.board[i][j-1]==self.word[idx+1]) 
            and self.search(i, j-1, idx+1)):
            return True
        
        if (i < len(self.board)-1 and self.visited[i+1][j]==0 and (self.board[i+1][j]==self.word[idx+1]) 
            and self.search(i+1, j, idx+1)):
            return True
        
        if (j < len(self.board[0])-1 and self.visited[i][j+1]==0 and (self.board[i][j+1]==self.word[idx+1]) 
            and self.search(i, j+1, idx+1)):
            return True
        
        # mark as again unvistited - if we not find pattern, so that same word can use in another row search
        self.visited[i][j] = 0
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        
        rows = len(board)
        cols = len(board[0])
        self.visited = [[0]*cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and self.search(i, j, 0):
                    return True
        return False

obj = Solution()
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','F']]
word = 'ABCCED'
obj.exist(board, word)

# =========================================================================

