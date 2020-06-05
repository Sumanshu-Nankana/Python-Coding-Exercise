#!/usr/bin/env python
# coding: utf-8
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

 

Note:

    1 <= costs.length <= 100
    It is guaranteed that costs.length is even.
    1 <= costs[i][0], costs[i][1] <= 1000
# In[ ]:


# we will follow below approach
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Lets send them all to city 'A'
# Total Cost: 10 + 30 + 400 + 30 = 470
# Now, we need to send half of them to city 'B' but which candidate we can send.
# Start from first and check till end
# if we send 1st ==> 10 + 30 + 400 + 30 = 470
                    +10
    
# if we send 2nd ==> 10 + 30 + 400 + 30 = 470
                    +10 +170
    
# if we send 3rd ==> 10 + 30 + 400 + 30 = 470
                    +10 +170  -350
    
# if we send 4th ==> 10 + 30 + 400 + 30 = 470
                    +10 +170 -350 -10
    
# total candidates are 4 (are right now all in CITY A)
# So we need to send half of the i.e. 2 in city B
# Pick minimum element i.e. -350 (and send this candidate to city B)
# then pick next minimum element i.e. -10 (and send this candidate to city B)
# and now stop (because we already sent 2 candidates)

# So output is - 110

# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.


# In[17]:


# Accepted in Leetcode

import sys
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        city_A = []
        for i in costs:
            city_A.append(i[0])
        
        final_cost = sum(city_A)
        
        city_B = []
        for j in costs:
            city_B.append(j[1]-j[0])
        
        for _ in range(len(costs)//2):
            min_ = min(city_B)
            final_cost += min_
            index = city_B.index(min_)
            city_B[index] = sys.maxsize
        
        return final_cost
            
        
obj = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
obj.twoCitySchedCost(costs)

