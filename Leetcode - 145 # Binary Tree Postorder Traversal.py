# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# postorder : Left ==> Right ==> Root

# Recursion
class Solution:
    def postorder(self, root, output):
        if root:
            self.postorder(root.left, output)
            self.postorder(root.right, output)
            output.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.postorder(root, output)
        return output


# Iterative
# We will take 2 stacks
# We will POP from 1st and push into second
# at the end , in Stack-2 all the elements will be required order from end to starting.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return
        stack1 = []
        stack2 = []

        stack1.append(root)
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node.val)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        return stack2[::-1]

