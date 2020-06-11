# Given an array with n objects colored red, white or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, 
# white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:

#     A rather straight forward solution is a two-pass algorithm using counting sort.
#     First, iterate the array counting number of 0's, 1's, and 2's, 
#     then overwrite array with total number of 0's, then 1's and followed by 2's.
#     Could you come up with a one-pass algorithm using only constant space?

# ==================================================================================
# Accepted in Leetcode

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # l = left pointer (where 0 needs to be inserted)
        # r = right pointer (where 2 needs to be inserted)
        # p = iterative pointor
        
        l, r, p = 0, len(nums)-1, 0
        while (p<=r):
            if nums[p] == 2:
                nums[p], nums[r] = nums[r], 2
                r = r - 1
            elif nums[p] == 0:
                nums[p], nums[l] = nums[l], 0
                l = l + 1
                p = p + 1
            else:
                p = p + 1
        return nums

# ==================================================================================