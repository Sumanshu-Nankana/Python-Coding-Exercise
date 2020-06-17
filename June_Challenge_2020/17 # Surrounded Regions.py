# Given a 2D board containing 'X' and 'O' (the letter O), 
# capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X

# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

# Explanation:

# Surrounded regions shouldn’t be on the border, 
# which means that any 'O' on the border of the board are not flipped to 'X'. 
# Any 'O' that is not on the border and it is not connected to an 'O' on 
# the border will be flipped to 'X'. 
# Two cells are connected if they are adjacent cells connected horizontally or 
# vertically.

# ===============================================================================
# Accepted in Leetcode
# Approach:
# We check all the 'O' which are on border and with border
# and mark all those 'O' with some other character
# Now we run a loop - to change all left 'O' to 'X'
# and that another character back to 'O'

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        self.board = board
        
        rows = len(board)
        if rows <=2: return board
        
        cols = len(board[0])
        if cols <=2: return board
        
        for row in range(rows):
            for col in range(cols):
                if (row==0 or row==rows-1 or col==0 or col==cols-1) and board[row][col]=='O':
                    self.dfs(board, row, col)
        
        for row in range(rows):
            for col in range(cols):
                
                if board[row][col]=='O':
                    board[row][col]='X'
                    
                elif board[row][col]=='B':
                    board[row][col]='O'
                    
                else:
                    pass
        return board
    
    def dfs(self, board, row, col):
        if (row>=0 and row<len(board) and col>=0 and col<len(board[0]) and board[row][col]=='O'):
            board[row][col] = 'B'
            
            self.dfs(board, row+1, col)
            self.dfs(board, row-1, col)
            self.dfs(board, row, col+1)
            self.dfs(board, row, col-1)

# ======================================================================================