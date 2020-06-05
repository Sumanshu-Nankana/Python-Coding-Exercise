#!/usr/bin/env python
# coding: utf-8

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# 
#  
# 
# Example 1:
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# Example 2:
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# Example 3:
# Input:s1="adc" s2 = "dcda" 
# Output: True
# 
# Note:
# 
#     The input strings only contain lower case letters.
#     The length of both given strings is in range [1, 10,000].
# 

# Below Code will work - But for large Inputs - It take time and Leetcode will not accept the code
# and fail with 'Time Limit Exceeded'

# In[15]:


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        temp = s1
        for i in range(len(s2)-len(s1)+1):
            for j in range(i, i+len(s1)):
                if s2[j] in temp:
                    temp = temp.replace(s2[j],'',1)
                    if temp == '':
                        return True
                else:
                    temp = s1  
                    break
        return False
                

obj = Solution()
s1 = input()
s2 = input()
print(obj.checkInclusion(s1, s2))

We will maintain a count of all 26 english chars by taking reference of s1:
example:s1: 'abc'   s2: 'cbaebabacd'
s1_count = [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

and now we need to find 1 'a' and 1 'b' in 's2'
when we found - we decrement s1_count and if all s1_count = 0 - it means we found the string and return True

So we first run the loop on 's2' by len(s1)
So lets traverse 's2' starting from index=0
First 'c'  -- decrease s1_count - s1_count = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
next 'b' -- decrease s1_count - s1_count = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
next 'a' -- decrease s1_count - s1_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Now we traverse 's2' for length of s1 --
Now check s1_count --> if any value is !=0 then break it , no need to check further.
and if all values are 0 -- we return True

Let's suppose above did not return True...So we need to check next window of 's2' of length 's1' i.e. 'bae'
check 'b' -- decrease s1_count -- s1_count = [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
check 'a' -- decrease s1_count -- s1_count = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
check 'e' -- decrease s1_count -- s1_count = [0,0,1,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
now window size over - now time to check s1_count as all are not zero -- so we break

Now we will shift the window of 's2' of length 's1' i.e. 'aeb'

But everytime, we don't need to check all the characters...In every window -- only 1 character added and 1 character removed..
So, we will decrease the count of newly introduced character and increase the count of removed character..
no need to check rest characters - as we already checked in earlier iterations.
# In[27]:


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        # lets initialize s1_count list with all 0's
        s1_count = [0]*26
        
        # Now increment the count by 1 for every character
        # we can get index of character by subtracting ord('a') from that ord('char')
        for ch in s1:
            s1_count[ord(ch) - ord('a')] +=1
        
        # Initially we will run 1 loop for size len(s1) on s2
        # and whatever character we found we decrement by 1
        start = 0
        for i in range(len(s1)):
            s1_count[ord(s2[i]) - ord('a')] -= 1
        
        # Now after 1 loop, check s1_count if all are '0'
        # if all are '0' return True
        match = True
        for ch in s1_count:
            if ch!=0:
                match = False
                break
        
        # if all are 0's then match will be true then retrun True
        # else ..look at the next window of s2 of length s1
        if match:
            return True
        else:
            start+=1
        
        # Now we need to look at all others windows
        while(start<=len(s2)-len(s1)):
            # as we shift the window, so earlier character removed
            # so we need to increase the count of earlier removed character
            idx1 = ord(s2[start-1]) - ord('a')
            s1_count[idx1]+=1
            
            # and for the newly added character in window
            # we will decrease the count
            idx2 = ord(s2[start+len(s1)-1]) - ord('a')
            s1_count[idx2]-=1
            
            # Now again check if all values in s1_count==0
            match=True
            for ch in s1_count:
                if ch!=0:
                    match = False
                    break
            if match:
                return True
            else:
                start+=1
        return False        
    
obj = Solution()
s1 = input()
s2 = input()
print(obj.checkInclusion(s1, s2))

