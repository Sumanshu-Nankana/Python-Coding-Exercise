# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note:  

#     1 is typically treated as an ugly number.
#     n does not exceed 1690.

# ========================================================================
# Not Accepted in Leetcode
# Time Limit Exceeded for Large Number example n = 373
# Approach - We will take a count variable and run a loop till count equal to Nth number
# as 1 is a ugly number
# So we will start checking from 2
# We can't just simply check whether N%2==0 or N/2 ==1
# because for example number 14 which is not a ugly number
# if we do 14%2=7 So, Now we need to check whether 7 is divisible by 2, 3, 5

class Solution(object):
    def maxDivide(self, a, b):
        while a%b==0:
            a = a/b
        return a
        
    def isUgly(self, num):
        num = self.maxDivide(num, 2)
        num = self.maxDivide(num, 3)
        num = self.maxDivide(num, 5)
        if num == 1: 
            return 1
        else:
            return 0
    
    def nthUglyNumber(self, n):
        count = 1
        i = 1
        while count < n:
            i+=1
            if self.isUgly(i):
                count+=1
        return i              
                
obj = Solution()
n = 0
print(obj.nthUglyNumber(n))

# ==============================================================================
# Accepted in Leetcode
# Approach - Dynamic Programing
# 2*1 = 2  3*1=3    5*1=5
# 2*2 = 4  3*2=6    5*2=10
# 2*3 = 6  3*3=9    5*3=15
# 2*4 = 8  3*4=14   5*4=20
# 2*5 = 10 ..       ..
# 2*6 = 12 ..       ..
# we will take a three variable i1, i2, and i3
# i1 is for 2th table
# i2 is for 3th table
# i3 is for 5th table
# Now we take an array and out '1' inside it as '1' is a ugly number
# Ugly [1]
# Now we will check minimum of (2,3,5) (i.e. first element of all table)
# So we put '2' in uglu array  [1,2]
# Minimum is from 2nd table so we will increment i1 conuter
# Now we will compare (4,3,5)
# minium is 3
# so we put '3' in ugly array [1,2,3]
# as minimum is form 3rd table, so we will increment i2
# Now compare min(4,6,10)
# min is 4
# Now add '4' into ugly array [1,2,3,4]
# and so on....

class Solution(object):
    # Function to get the nth ugly number 
    def nthUglyNumber(self, n): 

        ugly = [0] * n # To store ugly numbers 

        # 1 is the first ugly number 
        ugly[0] = 1

        # i2, i3, i5 will indicate indices for 2,3,5 respectively 
        i2 = i3 =i5 = 0

        # set initial multiple value 
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        # start loop to find value from ugly[1] to ugly[n] 
        for l in range(1, n): 

            # choose the min value of all available multiples 
            ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 

            # increment the value of index accordingly 
            if ugly[l] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if ugly[l] == next_multiple_of_3: 
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if ugly[l] == next_multiple_of_5:  
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        # return ugly[n] value 
        return ugly[-1] 

# ==============================================================================