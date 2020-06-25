# Given an array nums containing n + 1 integers 
# where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: [3,1,3,4,2]
# Output: 3

# Note:

#     You must not modify the array (assume the array is read only).
#     You must use only constant, O(1) extra space.
#     Your runtime complexity should be less than O(n2).
#     There is only one duplicate number in the array, 
#     but it could be repeated more than once.


# =============================================================================


#
# Below approach worked - But we modify the array and we can't revert to original array
# In question it's given - You must not modify the array 
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]

# ===================================================================================
# Accepted in Leet code

# if the length of array is 5 ; 
# the number contains it - is only between 1-4 (not even 0 or not 5 and 1 duplicate)
# nums = [1,3,4,2,2]
# and their index are 0,1,2,3,4
# so numbers in array are also a valid index. (all numbers from 1 to 4) and in index numbers are form 0-4 only

# we scan the array; 
# So we encountred '1' -- So we go to index 1 and add size of array ==> [1,8,4,2,2]
# Now we encountered '3' -- So we go to index 3 and add size of array ==> [1,8,4,7,2]
# Now we encountered '4' -- So we go to index 4 and add size of array ==> [1,8,4,7,7]
# Now we encountered '7' as its already modified, so we took mod 7%5  which is 2 ==> [1,8,9,7,7]
# Now we encountered '7' as its already modified, so we took mod 7%5  which is 2 ==> [1,8,14,7,7]

# Now we scan this modified array i.e. [1,8,14,7,7]
# and the find the index of maximum value which 14 and its index is '2'
# Along with that we will revert the modified array to original numbers just by taking mod
# 1%5 = 0
# 8%5 = 3
# 14%5 = 4
# 7 % 5 = 2
# 7 % 5 = 2
# So we placed original array as is [0,3,4,2,2]
# and while scanning, we store the index of max_value
# and return the index of max_value

# So our duplicate value is '2'

# In this though we modify the array - but at the end our array is same as of original one

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_idx = 0
        curr_max = 0
        
        for i in range(n):
            if nums[i] > n:
                id_ = nums[i]%n
            else:
                id_ = nums[i]
                
            nums[id_] += n
        
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
                max_idx = i
            
            nums[i] %= n
        
        return max_idx
    
obj = Solution()
nums = [1,3,4,2,2]
obj.findDuplicate(nums)

# =====================================================================================