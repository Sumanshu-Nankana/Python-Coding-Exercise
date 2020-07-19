# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, 
# for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, 
# return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .

# Example 2:

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. 
#              To take course 3 you should have finished both     
#              courses 1 and 2. 
#              Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. 
#              Another correct ordering is [0,2,1,3] .

# Note:

#     The input prerequisites is a graph represented by a list of edges, 
#     not adjacency matrices. Read more about how a graph is represented.
#     You may assume that there are no duplicate edges in the input prerequisites.

# ================================================================

# Accepted in Leetcode

class Solution(object):
    
    def dfs(self, u):
        self.visited[u] = 1
        for v in self.adj[u]:
            if self.visited[v] == 1: return True
            if self.visited[v] == 0 and self.dfs(v): return True
        
        self.visited[u] = 2
        self.stack.append(u)
        return False
    
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.adj = [[] for i in range(numCourses)]
        # print(self.adj)  [[], [], [], []] (length depend on number of courses)
        
        for courses in prerequisites:
            self.adj[courses[1]].append(courses[0])
        
        #print(self.adj)  ([[1,2], [3], [3], []])  for prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        
        self.stack = []
        self.visited = [0]*numCourses
        
        for i in range(numCourses):
            if self.visited[i]==0 and self.dfs(i):
                return []
        
        self.stack.reverse()
        return self.stack
            
    
obj = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
obj.findOrder(numCourses, prerequisites)

# ================================================================
