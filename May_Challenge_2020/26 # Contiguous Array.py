#!/usr/bin/env python
# coding: utf-8

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# 
# Note: The length of the given binary array will not exceed 50,000. 

# In[33]:


# Brute Force Method - Not Optimal
# Not accepted at LeetCode - Test Cases Failed with 'TIME LIMIT EXCEEDED'

class Solution:
    def findMaxLength(self, nums):
        dic_ = {}
        if len(nums) <= 1:
            return 0
        max_len = 0
        length = 0
        
        for i in range(len(nums)):
            zero_count = 0
            ones_count = 0
            if nums[i] == 0:
                zero_count += 1
            if nums[i] == 1:
                ones_count += 1
            for j in range(i+1, len(nums)):
                if nums[j] == 0:
                    zero_count += 1
                else:
                    ones_count += 1
                
                if zero_count == ones_count:
                    length = zero_count + ones_count

            if length > max_len:
                 max_len = length     

        return max_len
    
obj = Solution()
nums = [int(i) for i in input().split()]
print(obj.findMaxLength(nums))

we take a varible count and initialized it with 0
and we run 1 linear loop
if we found 0, we decrease count by 1  and if we found 1 , we increase count by 1
if we get count = 0 (it means till that point we have equal number of 0 and 1) - So max length is index+1
otherwise, we store the count as a Key in dictionary and value as index.
If key is already there - it means - we have subarray (from current index) and index of exiting key - which has equal number of 0 and 1
So to find max_length - we take max of existing value of max_length and that sub_array
# In[ ]:


# This is optimized and accepted in Leetcode
# for further explanation - https://www.youtube.com/watch?v=TSAN_SSAsos

class Solution(object):
    def findMaxLength(self, nums):
        dic = {}
        max_length = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count == 0:
                max_length = i+1

            if count in dic:
                max_length = max(max_length, i-dic[count])
            else:
                dic[count] = i

        return max_length

