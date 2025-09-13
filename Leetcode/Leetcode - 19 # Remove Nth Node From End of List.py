# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEndBruteForce(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # Step1 : Calculate the total number of elements in the Linked List
        # Step2: if N == Count (It means first element needs to be removed)
        # Step3: Else, Run a Loop Till Count - N elements (i.e. one element previous to the deleting element)
        # This Solution we are doing in 2 Passes (One Pass for Count and Other Pass for Removal)

        count = 0
        result = head

        # Get total number of nodes
        while head:
            count = count + 1
            head = head.next

        # if It's First node which needs to be deleted
        if n == count:
            return result.next

        # Run a Loop till the previous node (which needs to be deleted)
        diff = count - n
        i = 1
        new_head = result
        while i < diff:
            result = result.next
            i = i + 1
        else:
            result.next = result.next.next

        return new_head

    # Using Only One-Pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we will take the two-pointer (left, right) approach
        # and in starting - we will keep two pointers "n" distance far
        # and then we will keep increasing both pointer one by one
        # until right pointer reaches end.

        # The reason for putting two pointers "n" nodes far is
        # Now, if we increase both pointer
        # we can easily get the node (which needs to be deleted)

        # Using Two Pointer approach - we've  done this solution in ONE_PASS only.

        # take 2 pointers
        left = head
        right = head

        # put second pointer "n" nodes far
        for _ in range(n):
            right = right.next

        # if there is only 1 node
        if not right:
            return head.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head
