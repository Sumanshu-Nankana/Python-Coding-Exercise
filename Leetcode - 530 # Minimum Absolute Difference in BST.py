# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using Extra Space
# Create a List (Using Inorder Traversal)
# And we know, as we are cretaing using Inorder Travrsal (So List will be Sorted)
# Then To find the minimum between any two nodes - just subtract the alternate numbers
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp_list = []
        min_diff = float('inf')

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                temp_list.append(node.val)
                inorder_traversal(node.right)

        inorder_traversal(root)

        for i in range(len(temp_list) - 1):
            min_diff = min(min_diff, temp_list[i+1] - temp_list[i])
        return min_diff



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Without using extra Space
# Just instead of creating a list, we will do subtraction
# For the first node, there is no previous, thus we take it as None - and we will not
# do subtraction for first node.
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def inorder_traversal(node):
            nonlocal prev, min_diff
            if node:
                inorder_traversal(node.left)
                if prev:
                    min_diff = min(min_diff, (node.val - prev.val))
                prev = node
                inorder_traversal(node.right)

        inorder_traversal(root)

        return min_diff