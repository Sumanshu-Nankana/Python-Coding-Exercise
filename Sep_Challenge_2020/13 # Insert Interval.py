# Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# ===================================================================================

# Accepted in Leetcode

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in intervals:
            # existing interval not overlap with newInterval - so insert in output asis
            if i[1] < newInterval[0]:
                output.append(i)
            # 
            elif newInterval[1] < i[0]:
                output.append(newInterval)
                newInterval = i
            # Overlapping case , existing interval overlap with newInterval - We took startpoint as minimum of both
            # and endpoint as maximum of both
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        output.append(newInterval)
        return output
                
# ===============================================================================

# Accepted in Leetcode

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        output = []
        i, n = 0, len(intervals)
        
        # insert all non-overlapping intervals (which came before overlapped)
        while i<n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i+=1
        
        # make a new merged Interval and insert into output
        mI = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            i+=1
        output.append(mI)
        
        # Now insert all non-overlapping intervals (which came after overlapped)
        while i<n:
            output.append(intervals[i])
            i+=1
        
        return output

# ================================================================================