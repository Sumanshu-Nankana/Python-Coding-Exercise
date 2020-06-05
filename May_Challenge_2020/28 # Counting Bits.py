#!/usr/bin/env python
# coding: utf-8
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

# In[40]:


# Accepted in Leetcode - But still this is not optimized as it takes O(n*size_of_num)

class Solution:
    def countBits(self, num):
        output = []
        for i in range(0, num+1):
            count = 0
            while i!=0:
                rem = i%2
                i = i//2
                if rem==1:
                    count+=1
            output.append(count)
        return output
    
obj = Solution()
num = int(input())
print(obj.countBits(num))

# We can optimized it as we know
# Least significant bit of even numbers is 0
# least significant bit of odd numbers is 1
# Number of 1's in 23 (10111) and 46 (101110) same same.  - just difference is least signifcant bit in even is 0 and least significant bit in odd numbers is 1
# Number of 1's in 3 (0011) and 6 (110) are same


# In above solution - we are calculating number of 1's for all numbers..
# But actually there is no need for calculating number of 1's for all numbers - just we need to calc for n/2 
# numbers

# But if given number is even, just return its half
# but if given number is odd, just retun half(number) + 1

# So we can solve this by considering as Dynamic Problem
# and we will use right-shift operator by 1 OR we can use //2 -- to half the number (both give same result)
# In[43]:


# Accepted in Leetcode - and this more optimized and done in O(n)
# using // (int divide) operator 

class Solution:
    def countBits(self, num):
        bit_counts = [0]*(num+1)
        for i in range(1, num+1):
            bit_counts[i] = bit_counts[i//2] + i%2
            
        return bit_counts
    
obj = Solution()
num = int(input())
print(obj.countBits(num))


# In[44]:


# Accepted in Leetcode - and this more optimized and done in O(n)
# using right shift operator - Right shift operator even more faster than //

class Solution:
    def countBits(self, num):
        bit_counts = [0]*(num+1)
        for i in range(1, num+1):
            bit_counts[i] = bit_counts[i>>1] + i%2
            
        return bit_counts
    
obj = Solution()
num = int(input())
print(obj.countBits(num))

