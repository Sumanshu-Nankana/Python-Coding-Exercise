# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Using Recursion
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return None

        if root.val == targetSum and root.left is None and root.right is None:
            return True

        hashPathOnLeft = self.hasPathSum(root.left, targetSum - root.val)
        hasPathOnRight = self.hasPathSum(root.right, targetSum - root.val)

        return hashPathOnLeft or hasPathOnRight


# Using Iteration
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return None

        stack = [(root, targetSum - root.val)]

        while stack:
            node, current_sum = stack.pop()

            if node.left is None and node.right is None and current_sum == 0:
                return True

            if node.left is not None:
                stack.append((node.left, current_sum - node.left.val))

            if node.right is not None:
                stack.append((node.right, current_sum - node.right.val))

        return False
