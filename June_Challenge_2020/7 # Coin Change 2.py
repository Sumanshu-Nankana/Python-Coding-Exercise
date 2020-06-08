# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.

# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:

# Input: amount = 10, coins = [10] 
# Output: 1

# Note:

# You can assume that

#     0 <= amount <= 5000
#     1 <= coin <= 5000
#     the number of coins is less than 500
#     the answer is guaranteed to fit into signed 32-bit integer

# ==========================================================================
# Explanation - https://www.youtube.com/watch?v=UZ5QK-UV8MI&feature=youtu.be
# Method Lets suppose amount is 3
# Coins are [1, 2]
# Lets Draw Tree
# Total amount is 3 (and coins are of 1 and 2)
# So we can use 1rs coin and we can also use 2 rs coin

# ** LAYER1 **
# if we use 1rs coin , 2rs left 
# and we use 2rs coin, 1 rs left

# ** LAYER2 **
# Now, follow same approach on amount 2 and 1
# For amount '2', we can either use 1 rs or 2 rs
# if we give 1 rs, 1 rs left
# and we give 2rs, 0 rs left 
# Similarly, for amount 1
# if we give 1 rs ; 0 rs left
# and if we give 2 rd ; -1 left

#  ** Layer3 **
# we have amount 1
# if we use 1 rs ; 0 rs left
# if we use 2 rs ; -1 rs left

#                               3
#      2(if we give 1 rs coin)          1 (if we give 2 rs coin)
#
#   1     0                          0     -1
#
# 0   -1

# output are those 3 paths where we get 0
# i.e. 3---2---0       (here coin used as - [1,2])
#      3---2---1---0   (here coin used as - [1,1,1])
#      3---1---0       (here coin used as - [2,1])

# in this way we get answer 3 ; but actual answer is 2
# if we see above values are repeated - as we used PERMUTATION

# So, we need to use COMBINATION method  - So that values not repeat
#                                3
#                   2                          1
#           1              0             NA           NA
#     0          -1

# Now output is [3--2--1--0] i.e. (coins used [1,1,1])
#               [3--2--0] i.e. (coin used [1,2])

# What we did is ; when on first layer we divide the coins i.e.
# left hand side 1, right hand side 2
# which means Left hand side can use coins [1,2]
# right hand side can use coins [2] and can't use coin 1 (this prevent repetition)

# let's solve this problem by recursion
# our base case is if amount is 0, return
# and if amount is negative then return

# Below colution 17/27 test cases passed, rest failed with TIME LIMIT EXCEEDED
# class Solution(object):
#     def change(self, amount, coins):
#         if amount==0:
#             return 1
#         if amount < 0:
#             return 0
        
#         res = 0

#         for i in range(len(coins)):
#             res += self.change(amount-coins[i], coins[i:])
        
#         return res


# use dynamic Programming

# Accepted in Leetcode

class Solution(object):
    def change(self, amount, coins):
        size = len(coins)

        # Declaring a 2-D array
        # for storing solutions to subproblems:
        arr = [[0] * (amount + 1) for x in range(size + 1)]

        # Initializing first column of array to 1
        # because a sum of 0 can be made
        # in one possible way: {0}
        for i in range(size + 1):
            arr[i][0] = 1

        # Applying the recursive solution:
        for i in range(1, size + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:  # Cannot pick the highest coin:
                    arr[i][j] = arr[i - 1][j]
                else:  # Pick the highest coin:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]

        return arr[size][amount]


# ==========================================================================
# Use the Dynamic Proramming Approach to solve this problem (more optimized)
# Accepted in Leetcode
# 
# class Solution(object):
#     def change(self, amount, coins):
#         """
#         :type amount: int
#         :type coins: List[int]
#         :rtype: int
#         """
#         dp = [0]*(amount + 1)
#         dp[0] = 1
#         for c in coins:
#             for j in range(c, amount+1):
#                 dp[j] += dp[j-c]
        
#         return dp[amount]

# obj = Solution()
# amount = int(input())
# coins = []
# print(obj.change(amount, coins))