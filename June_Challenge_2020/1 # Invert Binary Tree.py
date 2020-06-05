#!/usr/bin/env python
# coding: utf-8
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
# In[ ]:


# We can solve this problem using recursion
# First we store root.right in some temp variable
# then we change root.right = invertTree(root.left)
# then we root.left = invertTree(temp)


# In[ ]:


# Accepted in Leetcode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root == None:
            return root
        right = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(right)
        
        return root

