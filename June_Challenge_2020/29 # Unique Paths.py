# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:

# Input: m = 7, n = 3
# Output: 28

# Constraints:

#     1 <= m, n <= 100
#     It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

# =============================================================================
# Accepted in Leetcode
# We will make a grid and start bottom-up approach
#
class Solution(object):
    def uniquePaths(self, m, n):
        
        grid = [[0]*m for row in range(n)]
        
        # fill last row - as there is only 1 way - RIGHT (from any cell of last row)
        for i in range(m):
            grid[n-1][i] = 1
        
        # fill last col - as there is only 1 way - DOWN (from any cell of last col)
        for j in range(n):
            grid[j][m-1] = 1
        
        
        # Now fill all others cell - which are sum of 
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                grid[i][j] = grid[i][j+1] + grid[i+1][j]
        
        return grid[0][0]
         
# ===========================================================================