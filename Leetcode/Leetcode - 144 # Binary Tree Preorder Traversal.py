# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Preorder : Root -- Left -- Right
# Recursive Solution
class Solution:
    def preorder(self, root, output):
        if root:
            output.append(root.val)
            self.preorder(root.left, output)
            self.preorder(root.right, output)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.preorder(root, output)
        return output


# Iterative Solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []

        if root is None:
            return

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            output.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output
