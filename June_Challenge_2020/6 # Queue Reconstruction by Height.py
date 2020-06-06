# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), 
# where h is the height of the person and k is the number of people in 
# front of this person who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# Accepted in leetcode
# Approach - Sort the people on basis of height (decreasing order)
# if two people heights are equal, the sort on 2nd parameter
# Then check every element, and put into at correct index (i.e. number of people should be in front)

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        people = sorted(people, key=lambda i: (-i[0],i[1]))

        for ppl in people:
            output.insert(ppl[1], ppl)
        return output

obj = Solution()
people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
print(obj.reconstructQueue(people))

# output - [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
