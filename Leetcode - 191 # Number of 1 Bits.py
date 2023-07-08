class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1:
                count = count + 1
            n >>= 1  # or we can do (n = n >> 1)
        return count