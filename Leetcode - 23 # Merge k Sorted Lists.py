# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Naive Approach - Not very Optimal
class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        answer = l3

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next

        if l1:
            l3.next = l1

        if l2:
            l3.next = l2

        return answer.next


    # we will merge 2 lists
    # And store the output in list1 (0th position)
    # And then we will merge list1 with third1
    # And then we will merge list1 with fourth
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        j = 1
        n = len(lists)

        while j < n:
            # Storing the output at 0th Index
            lists[0] = self.mergeTwoLists(lists[0], lists[j])
            j = j + 1

        # returning the 0th Index
        return lists[0]






