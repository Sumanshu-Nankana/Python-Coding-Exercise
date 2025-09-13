# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# We know if there is a Tree and We traverse Inorder Traversal - Then it will give us
# Sorted Array

# Now, in this question, Sorted Array is Given
# So, It means (It is a Inorder Traversal of Tree is Given)
# Which means ROOT is the middle
# and ROOT.LEFT = is its left
# and ROOT.RIGHT is its right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root
