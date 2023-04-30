# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Approach
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self._find_min_node(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node