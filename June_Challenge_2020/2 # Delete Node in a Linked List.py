#!/usr/bin/env python
# coding: utf-8
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

 

Note:

    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.
# In[ ]:


# Here we can't access the previous node , we can access only the given node (which we need to delete)
# Also, we can acccess all next nodes further to the given node
# So, we follow simple trick, we copy the val of next node into given node and delete next node
# because we can easily access next node, example
# 1 --> 2---> 3 --->4--->5 ---> Null
# lets suppose we want to delete '3'
# We can access all nodes from 3 i,e. 3 --> 4 ----> 5
# So, if we copy the content of next node into 3 and then delete next node ; our task done.
# i.e. 1--->2 --->4 --->4 --->5 ---> Null
# then 1--->2 --->4 ---->5 ---> null (here actually , we deleted last 2nd element)


# In[ ]:


# Accepted in Leetcode . Time complexity is O(1) and Space complexity is O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        next_node.next = Null    # This step is not mandatory. But to free the memory we can do that

