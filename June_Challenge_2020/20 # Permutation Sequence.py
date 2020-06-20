# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, 
# we get the following sequence for n = 3:

#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"

# Given n and k, return the kth permutation sequence.

# Note:

#     Given n will be between 1 and 9 inclusive.
#     Given k will be between 1 and n! inclusive.

# Example 1:

# Input: n = 3, k = 3
# Output: "213"

# Example 2:

# Input: n = 4, k = 9
# Output: "2314"

# =========================================================================================

# Accepted in Leetcode - But using inbuilt function to find permutation

import itertools
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        _list = []
        for i in range(1, n+1):
            _list.append(str(i))
        
        permutation_object = itertools.permutations(_list)
        _list = (list(permutation_object))
        
        return ''.join(_list[k-1])

# ==============================================================================================

#  Another aproach = Using Recursion to get all permutations
#  Time Limit Exceeded = Not Accepeted in Leetcode  (for n = 9, k = 62716) and for other
#  many longer test cases

class Solution(object):
    
    def findPermutations(self, mystr):
        if len(mystr)==0 or len(mystr)==1:
            return [mystr]
        res = []
        for ele in mystr:
            permutations = self.findPermutations(mystr.replace(ele, ""))
            for permutation in permutations:
                res.append(ele + permutation)
        return res
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        mystr=''
        for i in range(1, n+1):
            mystr+=str(i)
        
        out = self.findPermutations(mystr)
        return ''.join(out[k-1])

# ===========================================================================================
# Accepted in Leetcode - More optimized
# Approach :
# example: n = 4, k = 9
# so all 4 digits permutations are :
# 1234, 1243, 1324, 1342, 1423, 1432   #keeping 1 as constant
# 2134, 2143, 2314, 2341, 2413, 2431   #keeping 2 as constant
# 3124, 3142, 3214, 3214, 3412, 3421   #keeping 3 as constant
# 4123, 4132, 4213, 4231, 4312, 4321   #keeping 4 as constant

# So, if we keep 1 as constant, remaining digits left are 3 (so total 6 combination possible)
# start with 1 = but our K is 9 - So definately our result string not started with 1

# So we will subtract first 6 from K => 9-6 = 3

# So if we keep 2 as constant, 6 comibination possible starting with 2
# and K which is 3 now < 6
# So now we know result string will be started as '2' and remaining digits left are 1,3,4
# So in digits array - we will remove that digits which we finalized here '2'
# and now we have 3 digits only, # So we reduce our factorial array as well

# and we will run the same process till len of result string == n

# for more explanation - https://www.youtube.com/watch?v=knTd0fgAo-0

class Solution(object):
    def getPermutation(self, n, k):
        fact = [1]*n      # store factorial of all digits
        digits = [1]*n    # store all digits
        for i in range(1, n):
            fact[i] = fact[i-1] * (i+1)
            digits[i] = i+1
        
        result = ""     # store result string
        
        while len(result) < n-1:
            repeat = fact[-2]
            next_digit = (k-1)//repeat
            result += str(digits[next_digit])
            digits.pop(next_digit)
            fact = fact[:-1]
            k = k % repeat
            if k == 0:
                for i in range(len(digits)-1, -1, -1):
                    result += str(digits[i])
        
        if len(result) < n:
            result += str(digits[0])
        
        return result

# ==================================================================================