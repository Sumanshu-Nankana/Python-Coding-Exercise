# Given an array of numbers nums, in which exactly two elements appear only once 
# and all the other elements appear exactly twice. Find the two elements 
# that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]

# Note:

#     The order of the result is not important. So in the above example, [5, 3] 
#     is also correct.
#     Your algorithm should run in linear runtime complexity. 
#     Could you implement it using only constant space complexity?

# ===============================================================
# Accepted in Leetcode
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # approach: use XOR to find the mixed value of targets and
        #           separate these two by compare with lowest bit

        mixed = 0
        for num in nums:
            mixed ^= num

        lowest_bit = mixed & -mixed

        first = second = 0
        for num in nums:
            if lowest_bit & num > 0:
                first ^= num
            else:
                second ^= num

        return [first, second]

# ==================================================================
