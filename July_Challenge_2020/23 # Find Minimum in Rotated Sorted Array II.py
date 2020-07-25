# Suppose an array sorted in ascending order is rotated at some pivot unknown to 
# you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1

# Example 2:

# Input: [2,2,2,0,1]
# Output: 0

# Note:

#     This is a follow up problem to Find Minimum in Rotated Sorted Array.
#     Would allow duplicates affect the run-time complexity? How and why?


# ========================================================================
# Accepted in Leetcode

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                    r = mid
            else:
                r = r-1
        return nums[l]
        

# =======================================================================

