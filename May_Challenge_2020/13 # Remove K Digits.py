#!/usr/bin/env python
# coding: utf-8
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
Approach -

1 - if k == len(num) or len(num) == 0 -- then return 0
2 - otherwise..we will remove number 1 by 1 till k = 0 and after removing 1 number we deccrese k
    example 1432219 and k = 3
    
    So lets start with 1 -- if we remove 1..number left is 432219
    so better compare 1 with 4...So next number i.e. 4 is > 1 So we will remove '4' first instead of 1
    now, again before removing '4' lets compare it with next number which is '3' so  4 > 3
    so lets remove 4 (we removed our first number) and number left is 132219
    
    Now '3' came at place of '4' So instead of starting from same position, we start from 1 position before
    because if number is 1402219  --and after removing 4 --number left is 102219....
    So instead of removing '0' we need to remove '1' thus we need to start 1 index before.
    
    and do same process till k = 0
    
# In[29]:


class Solution(object):
    def removeKdigits(self, num, k):        
        
        if k == len(num) or len(num)==0:
            return '0'
        else:
            i = 0
            while(k > 0):
                while(i < len(num)-1 and num[i] <= num[i+1]):
                    i += 1
                num_list = list(num)
                num_list.pop(i)
                num = ''.join(num_list)
                k-=1
                if i > 0:
                    i-=1
                else:
                    i=0
            return str(int(num))

s = Solution()
num = input()
k = int(input())
if len(num) >= 10002 or len(num) < k:
    print("Invalid Scenario")
else:
    print(s.removeKdigits(num, k))

