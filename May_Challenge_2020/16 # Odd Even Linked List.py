#!/usr/bin/env python
# coding: utf-8
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
# In[3]:


# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
   
class Solution(object):
    def oddEvenList(self, head):
        if (head is None or head.next is None):
            return head
        else:
            h_odd = head
            h_even = head.next
            odd = h_odd
            even = h_even
            while (even is not None):
                # for odd number of elements in linked list (like 3 elements, 5 elements, 7 elements)
                if (even.next is not None):
                    odd.next = even.next
                # for even number of elements linked list (like 2 elements, 4 elements, 6 elements)
                else:
                    odd.next = h_even
                    return h_odd
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = h_even
            return h_odd                    

