# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its bottom-up level order traversal as:

# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# ========================================================================

class Solution(object):
    def levelOrderBottom(self, root):
        if root is None: return []
        queue = []
        output = []
        queue.append(root)
        while len(queue):
            nodes = []
            for i in range(len(queue)):
                ele = queue.pop(0)
                nodes.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            output.insert(0,nodes)
        return output  

# ========================================================================
