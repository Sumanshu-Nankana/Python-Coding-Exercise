# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
class Solution:
    def detectCycleUsingExtraSpace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        while head:
            if head in s:
                return head
            else:
                s.add(head)
                head = head.next
        return None


    # We will use two pointers slow and fast to find the cycle
    # and when both the pointers met (That may or may not be the node which we want to return)
    # But that node is as of same distance from both HEAD and Meeting pointer (slow and fast)
    # Thus, we will run loop again by proceeding HEAD and SLOW pointer
    # and when they met - that is actual the cycle point
    # and we will return that node.
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while head!=None and fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    slow = slow.next
                    head = head.next
                return head
        return None