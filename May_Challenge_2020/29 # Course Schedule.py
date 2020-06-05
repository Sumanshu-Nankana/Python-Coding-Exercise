#!/usr/bin/env python
# coding: utf-8
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5

# We will check if graph is cyclic or not
# if it's cyclic i.e. edge is coming back to processed node..then return False
# if edge is approaching unvisited or completed node - then its not cyclic and Return True

# So, first we create a adjacency Matrix  -  which contains all neighbouring nodes
# examle number of courses = 4
[0,
 1,
 2,
 3]

Now, we create further matrix and linked to all numbers 

[
 0,  -- [1,3]
 1,  -- [None]
 2,  -- [3]
 3   -- [1]
]

# we will apply depth first search - graph algorithm
# In[ ]:


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        # Creating adjacency Matrix
        
        self.adj = [None]*numCourses
        
        for i in range(numCourses):
            self.adj[i] = []
        
        for pre in prerequisites:
            self.adj[pre[0]].append(pre[1])
        
        # create a visited array
        # 0 - unvisited , 1 - Being processed (i.e. all neighbours not visited)
        # 2 - completed (all neighbours processed)
        self.visited = [0]*numCourses
        for i in range(numCourses):
            if self.visited[i] == 0 and not self.dfs(i):
                return False
        return True
    
    def dfs(self, v):
        # i.e. if edge is again pointing to being processed node - then cycle in graph and return False
        if self.visited[v] == 1:
            return False
        
        # otherwise mark it being processed
        self.visited[v] = 1
        
        # and check adjacent nodes
        for ad in self.adj[v]:
            if not self.dfs(ad):
                return False
        
        # mark the node as completed visited
        self.visited[v] = 2
        
        return True
            

