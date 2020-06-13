# Given a set of distinct positive integers, 
# find the largest subset such that every pair (Si, Sj) of elements in this subset 
# satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]

# ===========================================================================
# First we will sort all the elements in increasing order
# Because to get a % b = 0 or b % a = 0 (first term should be bigger)
# So if we sort it, we only need to compare the elements with right
# input = [2,3,4,6,10,8,24]
# Sort Input = [2,3,4,6,8,10,24]
# Initally all elements have solution as
# [[2],[3],[4],[6],[8],[10],[24]]
# Now we will start from end i.e. 24 (and append the output in above index)
# for 24 --> Nothing is in right {24} So only 24 is largest subset
# for 10 --> lets check if 24 is multiple of 10 or 24%10==0 is yes, then append 10 in solution of 24
#            but 24 is not multiple of 10, so for 10 - subset is {10}
# for 8 --> 24 is multiple of 8 So subset is {8,24}
# for 6 --> 24 is multiple of 6, so subset is {6,24}
# for 4 --> 8 and 24 are multiple so two solutions: {4,8,24} and {4,24} - bur largest is {4,8,24}
# for 3 --> 6,24 --> {3,6,24} and {3,24} but largest is {3,6,24}
# for 2 --> 4,6,8,10,24 --> {2,4,8,24} ; {2,6,24} ; {2,8,24} ; {2,10} ; {2,24}
# final output is {2,4,8,24}
# 
# but in this time cpmplexity is nlogn(for sorting) + O(n^2) (to checking right elements)
# time complexity = O(n^2)
# Space complexity is also = O(n^2) (as we are storing result for each element
#

# We can optimized above approach using storing best index - rather than whole list
# This will improve space complexity
# =================================================================================

# Accepted in Leetcode
#
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        if n <= 1: return nums
        
        # Sort the Input list
        nums.sort()

        next_idx = [-1]*n
        sizes = [1]*n
        max_len = 1
        max_idx = 0

        for i in range(n-1, -1, -1):
            j = i + 1
            _max, _max_idx = 0, i
            while j < n:
                if nums[j] % nums[i] == 0 and sizes[j] > _max:
                    _max = sizes[j]
                    _max_idx = j
                j += 1

            if _max_idx != i:
                sizes[i] += sizes[_max_idx]
                next_idx[i] = _max_idx
                if _max + 1 > max_len:
                    max_len = _max + 1
                    max_idx = i
        
        curr = max_idx
        while curr >= 0:
            result.append(nums[curr])
            curr = next_idx[curr]
        
        return result

# ===============================================================================

