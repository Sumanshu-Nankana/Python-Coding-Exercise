# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# =================================================================================
# Accepted in Leetcode
# Approach - Dynamic Programming (We can use recursion as well)

class Solution(object):
    def numTrees(self, n):
        # if 0 node - Null Tree  and if 1 node - 1 Tree
        if n == 0 or n == 1:
            return 1
        
        # for others formula is
        # f(n) = summation of [ f(i-1)*f(n-i) ]   --> left_hand_side * righ_hand_side (of that node)
        # summation from i = 1 to n
        # i.e. consider every node as root node and then calculate number of BST Trees
        # We can use recrsion, but there are so many repetitive calls
        # So we use Dynamic Programming approach
        
        sol = [0]*(n+1)   # DP Array
        sol[0], sol[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(i):
                sol[i] += sol[j]*sol[i-j-1]
        
        return sol[n]
    
# ==================================================================================