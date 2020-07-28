# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# =======================================================
# Accepted in Leetcode

# postorder == Left--Right--Root
# Inorder == Left--Root--Right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree_rec(self, i1, i2, p1, p2):
        if i1>=i2 or p1>=p2: return None
        root = TreeNode(self.postorder[p2-1])
        it = self.inorder.index(self.postorder[p2-1])
        diff = it - i1
        
        root.left = self.buildTree_rec(i1, i1+diff, p1, p1+diff)
        root.right = self.buildTree_rec(i1+diff+1, i2, p1+diff, p2-1)
        return root
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        if n==0: return None
        self.inorder = inorder
        self.postorder = postorder
        
        return self.buildTree_rec(0, n, 0, n)
        
    
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# ==================================================================

