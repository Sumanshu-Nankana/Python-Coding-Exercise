# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Inorder = Left -- Root -- Right
# Recursive Solution
class Solution:
    def inorder(self, root, output):
        if root:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.inorder(root, output)
        return output


# Recursive Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def inorder(root):
            if root:
                inorder(root.left)
                output.append(root.val)
                inorder(root.right)

        inorder(root)
        return output


# Iterative Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.val)
            current = current.right
        return output


# Iterative Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        current = root

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current.val)
                current = current.right
            else:
                break
        return output
