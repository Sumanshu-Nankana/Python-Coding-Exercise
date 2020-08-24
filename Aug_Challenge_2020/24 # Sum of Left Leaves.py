# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. 
# Return 24.

# ========================================================================
# Accepted in Leetcode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def sumOfLeftLeaves(root, isLeft):
            if isLeft and root.left == None and root.right == None:
                self.sum += root.val
                return
        
            if root.left is not None: sumOfLeftLeaves(root.left, True)
            if root.right is not None: sumOfLeftLeaves(root.right, False)
        
        if root is None: return 0
        sumOfLeftLeaves(root, False)
        return self.sum

# =============================================================================
# Another Approach
# Accepted in Leetcode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def dfs(root):
            if root is None: 
                return 0
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.sum += root.left.val
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.sum

# ==============================================================================
