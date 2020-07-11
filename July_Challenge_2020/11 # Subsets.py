# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# ============================================================
# Accpeted in Leetcode
# Approach - Scan whole array 
# And append element to (each element of previous output)

class Solution(object):
    def subsets(self, nums):
        output = [[]]      # length is 1
        if len(nums)==0:
            return output
        
        for num in nums:
            n = len(output)
            for i in range(n):
                r = output[i] + [num]
                output.append(r)
        
        return output
    
obj = Solution()
nums = [1,2,3]
print(obj.subsets(nums))

# =========================================================================