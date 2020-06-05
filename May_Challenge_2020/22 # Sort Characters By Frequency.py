#!/usr/bin/env python
# coding: utf-8
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

# In[ ]:


# This is accepted in Leetcode - But it's not optimized

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        dic_ = {}
        for ch in s:
            if ch in dic_:
                dic_[ch] += 1
            else:
                dic_[ch] = 1
        
        c = Counter(dic_)
        output = ''
        for tup in c.most_common():
            for i in range(tup[1]):
                output = output+tup[0]
        return output


# In[31]:


# This is also accepted in Leetcode - and it's optimized

class Solution(object):
    def frequencySort(self, s):
        dic_ = {}
        for ch in s:
            if ch in dic_:
                dic_[ch] += 1
            else:
                dic_[ch] = 1
        
        list_ = []
        for key,value in dic_.items():
            list_.append([key,value])
        
        sortedlist = sorted(list_, key = lambda list_ : list_[1], reverse=True)
        
        output = ''
        for tup in sortedlist:
                output = output + tup[0]*tup[1]
        return output

obj = Solution()
s = input()
obj.frequencySort(s)


# In[49]:


# This is also accepted in Leetcode - and it's optimized

class Solution(object):
    def frequencySort(self, s):
        dic_ = {}
        for ch in s:
                dic_[ch] = dic_.get(ch, 0) + 1
        
        sortedlist = sorted(dic_.items(), key = lambda c : c[1], reverse=True)
        
        output = ''
        for tup in sortedlist:
                output = output + tup[0]*tup[1]
        return output

obj = Solution()
s = input()
obj.frequencySort(s)

