# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def hasCycleUsingExtraSpace(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

    # We will sue Two Pointers
    # First Pointer will Run by 2*x
    # Second Pointer will Run by 1*x
    # Then we will check whether First Pointer can catch the Second Pointer
    # Catch means - Both Pointer will point to same Node (at some time)
    # If It catches --> Then It means It has Cycle.
    def hasCycleFloydCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
