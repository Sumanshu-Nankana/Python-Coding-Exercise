#!/usr/bin/env python
# coding: utf-8
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

 

Note:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].
# In[23]:


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        
        dict_ = {}
        for pair in dislikes:
            if pair[0] in dict_:
                dict_[pair[0]].add(pair[1])
            else:
                dict_[pair[0]] = set([pair[1]])
            
            if pair[1] in dict_:
                dict_[pair[1]].add(pair[0])
            else:
                dict_[pair[1]] = set([pair[0]])
            
        
        seen = {}
        for i in range(1, N+1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in dict_:
                        for b in dict_[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a]+1) % 2
                                stack.append(b)
        return True

