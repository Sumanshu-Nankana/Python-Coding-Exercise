# Reverse bits of a given 32 bits unsigned integer.

# Example 1:

# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents 
# the unsigned integer 43261596, so return 964176192 which its binary representation 
# is 00111001011110000010100101000000.

# Example 2:

# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 
# represents the unsigned integer 4294967293, so return 3221225471 
# which its binary representation is 10111111111111111111111111111111.

 

# Note:

#     Note that in some languages such as Java, there is no unsigned integer type. In 
#     this case, both input and output will be given as signed integer type and 
#     should not affect your implementation, as the internal binary representation 
#     of the integer is the same whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. 
#     Therefore, in Example 2 above the input represents the signed integer -3 and 
#     the output represents the signed integer -1073741825.

 

# Follow up:

# If this function is called many times, how would you optimize it?

# ==================================================================
# Accepted in Leetcode
# Approach - 
# Example 00110
# Now we want last digit and put them at first place
# So first we check whether last digit is 1 or 0
# we will take 'AND' with 1 - if it's 1 then output will 1

# 00110 & 1 ==> last digit we got 0
# Now we right shift 'n' with 1 i.e. 0011
# 0011 & 1 ==> last digit we got 1
# again right shift 'n' with 1 i.e. 001
# 001 & 1 ==> Last digit we got 1
# again right shift 'n' with 1 i.e. 00
# 00 & 1 ==> last digit we got 0
# again right shift 'n' with 1 i.e. 0
# 0 & 1 ==> last digit we got 0

# so if we combine all last digits we get ==> [0,1,1,0,0] ==> which is reverse of original
# digits ; but output in form of list
#
# if we have digit 0000
# and we have to insert 0 or 1 ; we need to take OR
# 0000 OR 0 ==> 0000
# 0000 OR 1 ==> 0001
# Now again we need to insert some number either 0 or 1
# first we do left shift of number example number is 0001
# do left shift so it became 0010
# now do or with 1 or 0 (whatever we want to insert)
# 0010 or 0 ==> 0010
# 0010 or 1 ==> 0011 

# The same process we have to follow
# =================================================================================

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = result << 1
            n = n & 1
            result = result | 1
            n = n >> 1
        return result

# ====================================================================