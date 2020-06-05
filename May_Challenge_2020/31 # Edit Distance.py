#!/usr/bin/env python
# coding: utf-8
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')word1 = 'H O R S E'
word2 = 'R O S'
Output = 3

To achieve this, we follow below steps -

1) First we compare last character of word1 with last character of word2 ; if both are equal then no operation reuired ; and we further check for (M-1, N-1) ; where M = Length of word1 and N = Length of word2

2) But if last character of word1 and word2 are not equal - then we can do three operations
   a) Insert b)Delete c) Replace
   **INSERT** 
   if we do insert i.e. if we insert last character of word2 in word1 then length of word1 is m+1  , but now lat character of both word1 and word2 become equal - but operation performed is 1
   So 1 + calculate for (M, N-1)
   
   **DELETE**
   if we do delete i.e. if we delete last character of word1, operation performed is 1
   So 1 + calculate distance for (M-1,N)
   
   ** REPLACE**
   
   if we do replace i.e. we replace last character of word1 same as of word2 , 
   then operation performed is 1
   1 + calculate(M-1, N-1)
   
   and we find minimum of above all 3 i.e.
   
   MIN (ED(M,N-1), ED(M-1,N), ED(M-1,N-1))  ED is EDIT DISTANCE
   
So this is a recursion problem - Lets draw a tree - 

                                     (m,n)
                                     
            (m-1, n-1)              (m, n-1)             (m-1, n)
               
(m-2, n-2) (m-1, n-2) (m-2, n-1) |  (m-1, n-2) (m-1, n-1) (m, n-1)
        
                       
                       
So, we could see there are some repetations - So we will use DYNAMIC PROGRAMMING and store the result
in a (m+1, n+1) matrix
                                        

If we make matric of 4 columns, and 6 rows
Lets go row by row
Row-1, Col-1 ; word1 is blank "" and word2 is "" ; So 0 operations
Row-1, Col-2 ; word1 is blank "" and word2 is "R" ; So 1 operations (i.e. insert R)
Row-1, Col-3 ; word1 is blank "" and word2 is "RO" ; So 2 operations (i.e. insert R and O)
Row-1, Col-4 ; word1 is blank "" and word2 is "ROS" ; So 3 operations (i.e. insert R,O,S)
    
Row-2, Col-1 ; word1 is "H" and word2 is "" ; So 1 operation (i.e. Delete H)
Row-2, Col-2 ; word1 is "H" and word2 is "R" ; So we took (1 + minimum of (ED(M,N-1), ED(M-1,N), ED(M-1,N-1)))
Row-2, Col-3 ; word1 is "H" and word2 is "RO" ; So 1 operation (i.e. Delete H)
Row-2, Col-4 ; word1 is "H" and word2 is "ROS" ; So 1 operation (i.e. Delete H)

Row-4 and Col-2 (last word is equal i.e. R) So No operation - Thus we return (m-1,n-1) value i.e. 2

  _ R O S
_ 0 1 2 3 
H 1 1 2 3
O 2 2 1 2
R 3 2 2 2
S 4 3 3 2
E 5 4 4 3

So at end our answer is value of (m+1,n+1) Or (m,n)(if we start from index-0)

Explanation is here - https://www.youtube.com/watch?v=ZkgBinDx9Kg&t=1281s
# In[ ]:


# Accepted in Leetcode

class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                # fill the values in first row
                if i==0:
                    dp[i][j] = j
                # fill the values in first column
                elif j==0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]

