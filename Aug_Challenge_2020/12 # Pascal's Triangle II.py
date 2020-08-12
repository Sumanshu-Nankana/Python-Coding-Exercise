# Given a non-negative index k where k ≤ 33, 
# return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]

# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

# ===========================================================
# Accepted in Leetcode

# Approach :
# We know output array will be of size rowIndex+1
# Now we need to updated the same array; rowIndex times
# and we start from top and to update particular element ; we will add two numbers directy
# above it i.e. of previous row.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]*(rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j-1]
        
        return result
        
# ==============================================================