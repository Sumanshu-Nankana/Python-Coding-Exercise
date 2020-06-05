#!/usr/bin/env python
# coding: utf-8
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
The approach here is - we will print the INORDER traversal of Tree (i.e LEFT -- ROOT -- RIGHT)
So it will print in Sorted order and we store all elements in an array and after that we just find arr[k-1] element.

But, we can optimized it a little bit more - i.e. while doing INORDER TRAVERSAL OF TREE - increment the counter by '1' and when counter is equal to 'k' return that element and stop INORDER TRAVERSAL of TREEBelow Code Executed in 88ms
# In[ ]:


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        self.count = 0
        self.output = 0
        self.kthInorderTraversal(root, k)
        return self.output
    
    def kthInorderTraversal(self, root, k):
        if root.left != None:
            self.kthInorderTraversal(root.left, k)
        self.count += 1
        if self.count == k:
            self.output = root.val   
            return self.output
        if root.right != None:
            self.kthInorderTraversal(root.right, k)

Below Code Executed in 55ms. But Both Code accepted in Leetcode
# In[ ]:


class Solution(object):
    
    def kthSmallest(self, root, k):
        self.count = 0
        self.output = 0
        self.kthInorderTraversal(root, k)
        return self.output
    
    def kthInorderTraversal(self, root, k):
        if root is None:
            return None
        
        self.kthInorderTraversal(root.left, k)
        self.count += 1
        if self.count == k:
            self.output = root.val   
            return self.output
        self.kthInorderTraversal(root.right, k)

