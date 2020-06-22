# Given a non-empty array of integers, every element appears three times except for one, 
# which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3

# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

# ================================================================================
# Accepted in Leetcode
# But we used the extra space - In question - its mention NOT to use extra space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        for key, value in dic.items():
            if value==1:
                return key

# ===================================================================================

# Another approach

# We sort the array Example : [-2,-2,1,1,-3,1,-3,-3,-4,-2]
# So sorted array = [-4, -3, -3, -3, -2, -2, -2, 1, 1, 1]
# We check border case
# if first element is not equal to 2nd element - Then return 1st element

# Another border case Example : [0,1,0,1,0,1,99]
# Sorted array is - [0, 0, 0, 1, 1, 1, 99]
# if last element is not equal to second last element - then return last element
#
# If len of nums is ==1 , then return first element
#
# Rest all cases
# Example - [2,2,3,2,3,3,4,5,3,3,3,5,5]
# Sorted array is - [2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5]
# Now we started from i=1 and we check with it's previous element
# and then increment i by 3
# wherever we not find equal, we will return nums[i-1]

# Accepted in Leetcode

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        else:
            i = 1
            while i<<len(nums):
                if nums[i]!=nums[i-1]:
                    return nums[i-1]
                i+=3

# =====================================================================================

# 
# One more approach
# We will write all the numbers in binary (32 bit)
# and then count number of 1's in last bit of all number 
# ans then modulus the total count by 3, if we get any reminder, add that bit to answer last bit
# Now, again check last 2nd bit of all numbers and follow same approach for all 32 bits and 
# for all numbers
#
# Another approach - by using XOR and AND operator
#