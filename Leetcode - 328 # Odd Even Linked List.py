# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If there is Zero Node OR 1 Node or 2 Node
        # Then we will simply return Head
        if head is None or head.next is None or head.next.next is None:
            return head
        # For More than 2 Nodes
        # we are taking two pointers, odd and even
        odd = head
        even = head.next

        # This is because, at last we need to attach Odd pointer will the Starting of Even List
        # So, we need to save Even Head somewhere.
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        # connecting odd end with even starting
        odd.next = even_head
        return head