# Given an array w of positive integers, where w[i] describes the weight of index i, 
# write a function pickIndex which randomly picks an index in proportion to its weight.

# Note:

#     1 <= w.length <= 10000
#     1 <= w[i] <= 10^5
#     pickIndex will be called at most 10000 times.

# Example 1:

# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]

# Example 2:

# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. 
# Solution's constructor has one argument, the array w. pickIndex has no arguments. 
# Arguments are always wrapped with a list, even if there aren't any.

# ===========================================================================================
# Below approach has been followed
# example - we have given weight array as = [1, 3, 4, 5 2]
# There are 5 weights, so we can assume there are 5 boxes
# [Box1] [Box2] [Box3] [Box4] [Box5]
#    1      3      4      5     2
#      1      4      8      13     15  # weight at end of boxes
#   1     2,3,4   5,6,7,8  9,10,11,12,13   14,15
# i.e. Box 1 - contains 1 value i.e. 1
# Box 2 contains 3 values i.e. 2,3,4
# Box 3 contains 4 values i.e. 5,6,7,8
# Box 4 contains 5 values i.e. 9,10,11,12,13
# Box 5 contains 2 values i.e. 14,15

# Here Boxes are Index - and values are weights

# We will create an array of cummulative weights
# w_cum = [1, 4, 8, 13, 15]
# Now, we will use randint function to get random value between (1, 15) (i.e. till sum)
# Then, we search that random value in cummulative weight array
# example, we get random value as 9
# So, 9 > 8 ; So it lies in window 8-13
# So, index is 3
# In above example - # ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# this means Solution called ones (i.e. weight passes ones)
# and pickIndex calls any number of times, and for every call - we need to return index
# proporation to its weight
# ===========================================================================================


# Accepted in Leetcode
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w_cum = []
        self.sum = 0
        for i in w:
            self.sum += i
            self.w_cum.append(self.sum)

    def pickIndex(self):
        """
        :rtype: int
        """
        idx = random.randint(1, self.sum)
        return self.binarySearch(idx)
    
    def binarySearch(self, val):
        l = 0
        r = len(self.w_cum) - 1
        while (l < r):
            mid = int(l + (r-l)/2)
            if self.w_cum[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
