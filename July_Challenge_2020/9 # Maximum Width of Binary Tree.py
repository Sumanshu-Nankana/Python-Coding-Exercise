# Maximum Width of Binary Tree
# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. 
# The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes 
# (the leftmost and right most non-null nodes in the level, 
# where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 
# (5,3,null,9).

# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).

# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).

# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 
# (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.

# ===============================================================================
# Accepted in Leetcode
# Approach -
# We take an array or queue
# and insert a pair of Node and it's index
# if we consider index of root is 0 ; then its left index is at 2*0 + 1
# and its right index is at 2*0 + 2
# if we consider index of root is 1 ; then its left index is at 2*1 
# and its right index is at 2*1+1
# After inserting pair - we will pop and find difference of first index inserted and 
# last index inserted at particular level
# and our aim is to find the maximum difference


# But here is one issue - if we insert index numbe - the value of number grows 
# exponentially and this may gave memory error
# We know  9-6 or 3-0 = both give same result
# So while inserting index ; we deal the numbers accoridngly


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        queue = [[root,0]]
        result = 1
        while len(queue) > 0:
            count = len(queue)
            start = queue[0][1]
            end = queue[-1][1]
            result = max(result, end-start+1)
            for i in range(count):
                p = queue[0]
                idx = p[1] - start
                queue.pop(0)
                if p[0].left is not None: 
                    queue.append([p[0].left, 2*idx+1])
                if p[0].right is not None:
                    queue.append([p[0].right, 2*idx+2])
        return result

# ===================================================================================