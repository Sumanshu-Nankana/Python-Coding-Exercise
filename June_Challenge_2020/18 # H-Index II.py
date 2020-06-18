# Given an array of citations sorted in ascending order 
# (each citation is a non-negative integer) of a researcher, 
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# "A scientist has index h if h of his/her N papers have at least h citations each, 
# and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
#              received 0, 1, 3, 5, 6 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.

# Note:

# If there are several possible values for h, the maximum one is taken as the h-index.

# Follow up:

#     This is a follow up problem to H-Index, where citations is now guaranteed to be 
#     sorted in ascending order.
#     Could you solve it in logarithmic time complexity?

# ============================================================================
# Linear Approach - O(n) 
# Accepted in Leetcode

# Explantion via example: citations = [0,1,3,5,6]
# lets start from index 0 - how many papers have citations atleast 0 = 5
# Now index 1 - How many papers have citations atleast 1 => 4
# Now index 2 - how many papers have citations atleast 3 => 3
# Now index 4 - How many papers have citations atleast 5 => 2 (But this violate the condition)
# Because Number of atleast papers should be >= citation number (Here citation is 5 and paper only 2)
# So best answer is 3

# Another example: citations = [1,1,1,1,1,4,4,5,6]
# index0 - How many papers have citations atleast 1 => 9 ; h-index=1
# index1 - How many papers have citations atleast 1 => 8 (Please note we will only count next papers)
# idnex2 - How many papers have citations atleast 1 => 7 ; h-index=1
# index3 - How many papers have citations atleast 1 => 6 ; h-index=1
# index4 - How many papers have citations atleast 1 => 5 ; h-index=1
# index5 - How many papers have citations atleast 4 => 4 ; h-index=4
# index6 - How many papers have citations atleast 4 => 3  (violates the condition)
# so best answer is 4 (as we need to take the maximum h-index)
# as there are many citations which satisfy condition; but we need to pick max citations which satisfy the condition
# which is 4
# so h-index is 4 (i.e. number of next papers >= citation)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        i, n = 0, len(citations)
        while(i<n and n-i > citations[i]):
            i+=1
        return n-i      
        
    
# ===============================================================================

# Binary Search Approach - O(logn)
# Accepted in Leetcode

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, n = 0, len(citations)-1, len(citations)
        while (left<=right):
            mid = left + (right-left)//2
            if citations[mid] == n-mid:
                return n - mid
            elif citations[mid] > n-mid:
                right = mid-1
            else:
                left = mid+1
        return n-left
    
# ================================================================================

