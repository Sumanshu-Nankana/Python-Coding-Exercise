# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from queue import Queue


# Recursive approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecursiveSolution:
    def __init__(self):
        pass

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None and node2 is not None:
            return False
        if node1 is not None and node2 is None:
            return False
        if node1.val != node2.val:
            return False
        firstMirror = self.is_mirror(node1.left, node2.right)
        secondMirror = self.is_mirror(node1.right, node2.left)
        return firstMirror and secondMirror


class IterativeSolution:
    def __init__(self):
        pass

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = Queue()
        queue.put((root.left, root.right))

        while not queue.empty():
            node1, node2 = queue.get()
            if node1 is None and node2 is None:
                continue
            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            if node1.val != node2.val:
                return False
            queue.put((node1.left, node2.right))
            queue.put((node1.right, node2.left))

        return True
