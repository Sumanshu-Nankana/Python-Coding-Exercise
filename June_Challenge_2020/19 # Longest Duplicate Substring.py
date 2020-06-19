# Given a string S, consider all duplicated substrings: (contiguous) 
# substrings of S that occur 2 or more times.  (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.  
# (If S does not have a duplicated substring, the answer is "".)

# Example 1:

# Input: "banana"
# Output: "ana"

# Example 2:

# Input: "abcd"
# Output: ""

# Note:

#     2 <= S.length <= 10^5
#     S consists of lowercase English letters.

# =============================================================================================#
# We need to follow Binary Search and Rabin-Karp - Algorithm
# I just copied the code (from somewhere else) 

# Accepted in Leetcode

class Solution(object):
    def longestDupSubstring(self, S):
        p = 2**63-1
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash *26 + nums[i]) % p
            hashes ={cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)
            for i in range(mid, len(S)):
                cur_hash = (26*cur_hash-nums[i-mid]*max_pow + nums[i]) % p
                if cur_hash in hashes:
                    pos = i + 1 - mid
                hashes.add(cur_hash)
            return pos
        
        #bst
        nums = [ord(c) for c in S]
        l,r = 0,len(S)-1
        start,end = 0,0
        
        while (l<=r):
            mid = (l+r)//2
            pos = rabin_karp(mid)
            if pos == -1:
                r = mid - 1
            else:
                start,end = pos, pos+mid
                l = mid + 1

        return S[start:start+l-1]
                
obj = Solution()
S = input() # banana
print(obj.longestDupSubstring(S))

# ===========================================================================================