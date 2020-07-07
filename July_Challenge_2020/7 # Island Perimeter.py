# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" 
# (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# ============================================================================
# Accepted in Leetcode
# Approach - in starting we took permiter = 4 (considering all sides it has water)
# And then we will start decrementing parameter if the condition not mets
# like if not first row, not last column etc etc
class Solution(object):
    def islandPerimeter(self, grid):
        permimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    continue
                permimeter+=4
                if row>0: permimeter -= grid[row-1][col]
                if col>0: permimeter -= grid[row][col-1]
                if row<rows-1: permimeter -= grid[row+1][col]
                if col< cols-1: permimeter -= grid[row][col+1]
        return permimeter
        
# =======================================================================