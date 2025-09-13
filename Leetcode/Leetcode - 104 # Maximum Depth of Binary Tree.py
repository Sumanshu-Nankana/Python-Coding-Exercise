# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from queue import Queue


class RecursiveSolution:
    def __init__(self):
        pass

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        left_tree_depth = self.maxDepth(root.left)
        right_tree_depth = self.maxDepth(root.right)
        return 1 + max(left_tree_depth, right_tree_depth)


class IterativeSolution:
    def __init__(self):
        pass

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = Queue()
        queue.put((root, 1))
        max_depth = 0

        while not queue.empty():
            node, depth = queue.get()
            max_depth = max(max_depth, depth)

            if node.left:
                queue.put((node.left, depth + 1))
            if node.right:
                queue.put((node.right, depth + 1))

        return max_depth
