# Given a binary tree containing digits from 0-9 only, 
# each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Example:

# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:

# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# ============================================================================
# Accepted in Leetcode
# Approach - We will use recursion
# Base Cases:
# if root is None = return 0
# if root.left is None and root.right is None - it means output is that number itself
# So, we took one output = 0 and add that number into that.

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.output = '0'        # final output
        self.helper(root, '0')   # initial value pass as 0
        return self.output
    
    def helper(self, root, val):
        
        # Base case
        if root is None: return 0
        
        # whatever value we get from above (make a string) by adding current root value
        # i.e. we get '0' from above, and lets suppose at root its 3 ==> '03'
        
        val = str(val) + str(root.val)      # current valuefrom root to that node
        
        # Base case
        # if that is leaf node, we add that value by changing to integer and add to final output
        if root.left is None and root.right is None:
            self.output  = int(self.output) + int(val)
            return
        
        if root.left:
            self.helper(root.left, val)
        
        if root.right:
            self.helper(root.right, val)

# ======================================================================================