# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, 
# is completely filled, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6

# ========================================================================================
# Accepted in Leetcode
# Approach

# We know if we have complete binary tree
# Then Number of nodes in tree is 2^n -1 (where n is height of tree)
# So we will check left height of tree and right height of Tree
# and if both are equal - then its complete Binary Tree 
# and we will return 2^n -1

# But we know complete binary tree is that as well if all nodes in last level as far left
# as possible - like in above example
# So in that case 2^n-1 (formula will not work)

# So for such scenarios, we call the same function (on left subtree) and (on right Subtree)
# and count the nodes
# and after that add the nodes which we get from left sub-tree and right-sub-tree and 1 
# 1 (for root)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if root is None: return 0
        left, right = root, root
        left_height, right_height = 0, 0
        
        while left is not None:
            left_height += 1
            left = left.left
        
        while right is not None:
            right_height += 1
            right = right.right
        
        if left_height == right_height: return (1<<left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# ======================================================================================

# The other way is to PREORDER or INORDER or POSTORDER traversal of TREE
# and count the number of Nodes.
# But that is not effcient in that we took O(n) as we traverse all nodes

# But in above method, we are not traversing all nodes.
# We are only traversing few nodes and then we use the property of Complete Binary Tree

# ======================================================================================