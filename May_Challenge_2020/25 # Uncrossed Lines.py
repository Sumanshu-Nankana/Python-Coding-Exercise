#!/usr/bin/env python
# coding: utf-8

# We write the integers of A and B (in the order they are given) on two separate horizontal lines.
# 
# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
# 
#     A[i] == B[j];
#     The line we draw does not intersect any other connecting (non-horizontal) line.
# 
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
# 
# Return the maximum number of connecting lines we can draw in this way.
# 
#  
# 
# Example 1:
# 
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
# 
# <img src="uncrossedLine.png">
# 
# Example 2:
# 
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
# 
# Example 3:
# 
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
# 
#  
# 
# Note:
# 
#     1 <= A.length <= 500
#     1 <= B.length <= 500
#     1 <= A[i], B[i] <= 2000
# 
# 
We Will follow below approach -

Lets A = [] of length m
     B = [] of length n
    
we will compare last element of both A & B, If A[m] == B[n] then definately they will met
So, In next run we will check for  (1 + Fun(m-1, n-1))  # i.e. for remaining elements ; we add 1 for 1 last line
which we found by connecting last elements

if last elements did not match then,
we will check for All elements of A with (n-1) elements of B
and all elements of B with m-1 elements of A
and whoever give max result, we took that

max(Func(m,n-1), Func(m-1,n))

again we will follow same approach...so at some point we again found

Func(m-1,n-1) 

# but we already found func(m-1,n-1) in some other call - So if we found again, its not optmized solution,
Thus we will use Dynamic Programming solution.

For that, we need to take a 2D array and array will be initialized with 0 initially
and we will take a 2D array of size (m+1 , n+1)


We can either start from end or start from first...in below solution we started from first and thus return last value

#for further explanation - https://www.youtube.com/watch?v=jLv-5coG-qQ
# <img src="UncrossedLines.png">

# In[ ]:


# Accepted in Leetcode..

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
                
obj = Solution()
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(obj.maxUncrossedLines())

