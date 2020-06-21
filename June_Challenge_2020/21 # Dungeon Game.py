# The demons had captured the princess (P) and imprisoned her in the bottom-right 
# corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. 
# Our valiant knight (K) was initially positioned in the top-left room and must
# fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. 
# If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) 
# upon entering these rooms; other rooms are either empty (0's) or contain magic orbs 
# that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move 
# only rightward or downward in each step.

# Write a function to determine the knight's minimum initial health so that 
# he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight 
# must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
# -2 (K) 	-3 	3
# -5 	-10 	1
# 10 	30 	-5 (P)

 

# Note:

#     The knight's health has no upper bound.
#     Any room can contain threats or power-ups, even the first room the knight enters
#     and the bottom-right room where the princess is imprisoned.

# ============================================================================
# Accepted in Leetcode

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        r = len(dungeon)
        c = len(dungeon[0])
        
        # we will create a solution 2D array and update the cell
        # with value - that minimum health required to enter that cell
        sol = [[0]*c for i in range(r)]
        
        # So we will start from end
        # if last cell contains positive value that '1' as minimum health
        
        if dungeon[r-1][c-1] > 0:
            sol[r-1][c-1] = 1 
        else:
            sol[r-1][c-1] = 1-dungeon[r-1][c-1]
        
        # for last column
        for i in range(r-2, -1, -1):
            sol[i][c-1] = max(sol[i+1][c-1] - dungeon[i][c-1], 1)
        
        # for last row
        for j in range(c-2, -1, -1):
            sol[r-1][j] = max(sol[r-1][j+1] - dungeon[r-1][j], 1)
        
        # for rest cell
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                sol[i][j] = max(min(sol[i+1][j], sol[i][j+1])-dungeon[i][j], 1)
            
        return sol[0][0]
    
obj = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
obj.calculateMinimumHP(dungeon)

# =====================================================================================
