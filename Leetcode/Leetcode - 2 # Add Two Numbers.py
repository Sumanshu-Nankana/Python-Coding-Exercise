# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode()
        result = l3
        while l1 and l2:
            temp_sum = l1.val + l2.val + carry
            quo, rem = divmod(temp_sum, 10)
            l3.next = ListNode(rem)
            carry = quo
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp_sum = l1.val + carry
            quo, rem = divmod(temp_sum, 10)
            l3.next = ListNode(rem)
            carry = quo
            l3 = l3.next
            l1 = l1.next

        while l2:
            temp_sum = l2.val + carry
            quo, rem = divmod(temp_sum, 10)
            l3.next = ListNode(rem)
            carry = quo
            l3 = l3.next
            l2 = l2.next

        if carry > 0:
            l3.next = ListNode(carry)

        return result.next

    # Same approach - by reducing unncessary repeated conditions
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode()
        result = l3
        carry = 0

        while l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            temp_sum = value1 + value2 + carry
            quo, rem = divmod(temp_sum, 10)
            carry = quo

            l3.next = ListNode(rem)
            l3 = l3.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            l3.next = ListNode(carry)

        return result.next
