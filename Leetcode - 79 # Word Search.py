class Solution:

    def search(self, i, j, idx):
        if idx == len(self.word) - 1:
            return True

        self.visited[i][j] = 1

        # check upper side
        if (i>0 and self.visited[i-1][j]==0 and self.board[i-1][j]==self.word[idx+1]) and self.search(i-1, j, idx+1):
            return True

        # check down side
        if (i<self.rows-1 and self.visited[i+1][j]==0 and self.board[i+1][j]==self.word[idx+1] and self.search(i+1, j, idx+1)):
            return True

        # check right side
        if (j<self.cols-1 and self.visited[i][j+1]==0 and self.board[i][j+1]==self.word[idx+1] and self.search(i, j+1, idx+1)):
            return True

        # check left side
        if (j>0 and self.visited[i][j-1]==0 and self.board[i][j-1]==self.word[idx+1] and self.search(i, j-1, idx+1)):
            return True

        self.visited[i][j] = 0
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])

        self.visited = [[0]*self.cols for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == self.word[0] and self.search(i, j, 0):
                    return True
        return False