# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will 
# be at positions (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the 
# vertical line touches some nodes, we report the values of the nodes in order 
# from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is reported 
# first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  
# Every report will have a list of values of nodes.

 

# Example 1:

            3
      9           20

              15        7

# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).

# Example 2:

            1
     2              3
4        5     6          7

# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according to 
# the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller 
# than 6.

# ===============================================================================

# Accepted in Leetcode
# Approach: We process the tree DFS wise and we create a dictionary where key is the column
# and value is node_value

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None: return result
        cache = {}
        self.minCol = 0
        self.maxCol = 0
        
        def dfs(node, row, col):
            if node is None: return
            if col in cache:
                cache[col].append([row, node.val])
            else:
                cache[col] = [[row, node.val]]
            self.minCol = min(self.minCol, col)
            self.maxCol = max(self.maxCol, col)
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        
        for c in range(self.minCol, self.maxCol+1):
            col = sorted(cache[c], key=lambda x: (x[0],x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
        
        return result
            
# ===========================================================================

