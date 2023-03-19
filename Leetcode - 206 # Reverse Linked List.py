# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def reverseListIteratively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        previous = head
        current = head.next
        previous.next = None
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
        return previous

#   HELPER   HEAD      NEXT
#   NONE      1-------->2--------->3--------->4---------->5
    # We will keep track of previous node and next node
    # we will just reverse the pointers
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = None
        while head is not None:
            nextNode = head.next
            head.next = helper
            helper = head
            head = nextNode
        return helper



    # Recursion will take a lot of memory
    def reverseListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case
        if head is None or head.next is None:
            return head

        # calling the Same Function again (for Rest of the List - Until the Base Case Hit)
        reverseListHead = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return reverseListHead