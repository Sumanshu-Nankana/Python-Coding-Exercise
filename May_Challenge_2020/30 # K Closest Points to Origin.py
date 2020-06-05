#!/usr/bin/env python
# coding: utf-8
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

 

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000


# In[28]:


# 81 / 83 test cases passed. in Leetcode - Rest Failed with TIME LIMIT EXCEEDED

import math
class Solution(object):
    def kClosest(self, points, K):
        dic = {}
        output = []
        for point in points:
            y = (point[1] - 0)**2
            x = (point[0] - 0)**2
            distance = math.sqrt(y+x)
            dic[points.index(point)] = distance
        sorted_dic_list = sorted(dic.items(), key = lambda item: item[1])
        
        for i in sorted_dic_list[:K]:
            output.append(points[i[0]])
        
        return output
        
obj = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = int(input())
obj.kClosest(points, K)

# Another method is -
# We will first scan only 'K' points and calculate the distance
# and create a MAX_HEAP tree - So the point which has maximum distance at TOP

# Now we will scan from K+1 points to N points
# if distance of K+1 point is > MAX element of MAX_HEAP - we ignore that point
# if distance of K+1 point is < MAX element of MAX_HEAP - we remove MAX element from MAX_HEAP
# and insert new point - and again make sure tree is back in MAX_HEAP order
# such that MAX distance point is at TOP

# So, we follow same process till N
# and at END - in MAX_HEAP TREE - we only have K - Smallest point
# Now we pop one by one - and add into an output array.
# In[29]:


# This solution is accepted in LEETCODE

import heapq
class Solution(object):
    def kClosest(self, points, K):
        # we are string three values distance, point1(x) and point2(y)
        # pq is a priority queue
        pq = [[-x*x - y*y, x , y] for x, y in points[:K]]
        # by default it's a min-heap
        heapq.heapify(pq)
        
        for x,y in points[K:]:
            d = x*x + y*y
            # as its a min-heap so top element is minimum - thus we take negative of that
            if -pq[0][0] > d:
                heapq.heappush(pq, [-d, x, y])
                heapq.heappop(pq)
        
        return [[x, y] for d, x, y in pq]

