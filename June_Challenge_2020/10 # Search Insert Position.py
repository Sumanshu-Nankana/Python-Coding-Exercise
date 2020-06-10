# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2

# Example 2:

# Input: [1,3,5,6], 2
# Output: 1

# Example 3:

# Input: [1,3,5,6], 7
# Output: 4

# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

# ======================================================================================
# Accepted in leetcode

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, n in enumerate(nums):
            if n == target:
                return idx
            elif n > target:
                return idx
            else:
                pass
        return len(nums)

# =========================================================================================

# Another Solution - Using Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] < target:
                start = start + 1
            elif nums[mid] > target:
                end = end - 1
            else:
                return mid
        
        return start

# ======================================================================================

