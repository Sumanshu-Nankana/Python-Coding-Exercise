# In a given grid, each cell can have one of three values:

#     the value 0 representing an empty cell;
#     the value 1 representing a fresh orange;
#     the value 2 representing a rotten orange.

# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
# If this is impossible, return -1 instead.


# Example 1:

# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
# because rotting only happens 4-directionally.

# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

# Note:

#     1 <= grid.length <= 10
#     1 <= grid[0].length <= 10
#     grid[i][j] is only 0, 1, or 2.

# ====================================================================
# Accepted in Leetcode

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten = []
        r = len(grid)
        c = len(grid[0])
        fresh = 0
        t = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        while len(rotten) > 0:
            num = len(rotten)
            for i in range(num):
                x, y = rotten[0]
                rotten.pop(0)
                if x > 0 and grid[x-1][y]==1:
                    grid[x-1][y]=2
                    fresh -= 1
                    rotten.append([x-1, y])
                if y > 0 and grid[x][y-1]==1:
                    grid[x][y-1]=2
                    fresh -= 1
                    rotten.append([x, y-1])
                if x < r-1 and grid[x+1][y]==1:
                    grid[x+1][y]=2
                    fresh -= 1
                    rotten.append([x+1, y])
                if y < c-1 and grid[x][y+1]==1:
                    grid[x][y+1]=2
                    fresh -= 1
                    rotten.append([x, y+1])
            if len(rotten) > 0:
                t = t + 1
        
        return t if (fresh == 0) else -1

# ===================================================================