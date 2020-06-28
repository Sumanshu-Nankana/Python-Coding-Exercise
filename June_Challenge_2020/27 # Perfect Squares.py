# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# =====================================================================================

# n = 12
# Squares less than 12 = (1,4,9) ==> So output should contain either 1 or 4 or 9 or 
# all or any pairs
# Lets suppose if output contains 1 -- then remaining number is 11
# Lets suppose if output contains 2 -- then remaining number is 8
# Lets suppose if output contains 9 -- then remaining number is 3
                            
# Now We need to check all Sqaures less than 11 = (1,4,9)
# Now We need to check all Sqaures less than 8 = (1,4)
# Now We need to check all Sqaures less than 3 = (1)

# Now, 11 can be make using 1,4,9, lets take 1 by 1
# Similarly 8 can be made using 1, 4
# Similarly 3 can be made using 1

# Now take sqaures less than 10 = (1,4,9)
# Squares less than 7 = (1,4)
# and so on..
#                                           12
        
#                             11            8              3
        
#                     10      7    2   | 7      4  |     2
            
#                  9   6  1 |6  3 |1   |6  3  |3  0 |   1
                
#                 and so on.....
                
# So this is recursive approach..But we see like for 7 (we caclulate two times)
# For 6 ,we calculated 3 times - So overlapping sub-problems

# So at end - we will check we reach '0' in which least(minimum) steps is our answer
# So for 12 it's '3' (12-8 , 8-4, 4-4 ==> 4+4+4 )  3 steps

# So better to use dynamic programming approach

# Take a array - and save the number of least sqaures to form that number....
# So that we can use that - instead of re-calculating it

# ==================================================================================

# Recursion - Time Limit Exceeded - 47 / 588 test cases passed.

class Solution(object):
    def numSquares(self, n):
        return self.helper(n)
    
    def helper(self, n):
        # Base-cases
        if n <= 3:
            return n
        
        output = n                                      # Max n squares possible (with 1) for worst answer
        i = 1
        while i*i <= n:
            output = min(1+self.helper(n-i*i), output)
            i+=1
        
        return output
        
obj = Solution()
n = int(input())
print(obj.numSquares(n))

# =======================================================================================

# Recursion with Memoization = Accepted - 588 / 588 test cases passed. (But Runtime is worst of all submission)
# Also a Dynamic Programming

class Solution(object):
    def numSquares(self, n):
        self.dp = [0]*(n+1)
        return self.helper(n)
    
    def helper(self, n):
        # Base-cases
        if n <= 3:
            return n
        
        if self.dp[n]!=0:
            return self.dp[n]
        
        output = n                                      # Max n squares possible (with 1) for worst answer
        i = 1
        while i*i <= n:
            output = min(1+self.helper(n-i*i), output)
            i+=1
        
        self.dp[n] = output
        
        return output
        
obj = Solution()
n = int(input())
print(obj.numSquares(n))

# ========================================================================================

# Dynamic Programming - Tabulation = = Accepted - 588 / 588 test cases passed. 
# But Runtime is better than above , but still only 26 % better than other submission

class Solution(object):
    def numSquares(self, n):
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = i                    # Max i squares possible (with 1) for worst answer
            j = 1
            while j*j <= i:
                sq = j*j
                dp[i] = min(dp[i], 1+dp[i-sq])
                j+=1
        
        return dp[n]
        
obj = Solution()
n = int(input())
print(obj.numSquares(n))

# ==============================================================================

# Another Best approach is - Legendre's 3-sqaure Theorem - which will only take sqrt(n) time.