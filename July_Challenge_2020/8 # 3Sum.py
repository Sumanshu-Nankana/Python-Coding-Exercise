# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array which gives 
# the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# ======================================================================================
# Accepted in Leetcode
# Approach
# - we sorted the array
# - Then fixed first element and find pair in rest 
# - if we found pair we add in set (as we don't want duplicates pairs)
# - at the end return the list 

# But this is as not much efficient
# Because we are processing duplicates as well

class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        output = set()
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif sum_ > 0:
                    k = k -1
                else:
                    j = j + 1
            
        return list(output)
    
obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(obj.threeSum(nums))

# ================================================================================
# Accepted in Leetcode
# Approach - its same approach as above - with a little difference
# As we sorted the array
# So before processing next element, we are comparing that element with previous one
# if it's same, then we will skip that element
# It makes our code a little bit more optmized

class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        output = []
        for i in range(0, len(nums)-2):
            if (i==0 or nums[i]!=nums[i-1]):
                j = i+1
                k = len(nums)-1
                while j < k:
                    sum_ = nums[i] + nums[j] + nums[k]
                    if sum_ == 0:
                        output.append([nums[i], nums[j], nums[k]])
                        while (j<k and nums[j]==nums[j+1]):
                            j+=1
                        while (j<k and nums[k]==nums[k]-1):
                            k-=1
                        j+=1
                        k-=1
                    elif sum_ > 0:
                        k = k -1
                    else:
                        j = j + 1

        return list(output)
    
obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(obj.threeSum(nums))

# ===============================================================================