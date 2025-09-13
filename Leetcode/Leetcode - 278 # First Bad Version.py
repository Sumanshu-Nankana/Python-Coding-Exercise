# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersionBruteForce(self, n: int) -> int:
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i

    def firstBadVersionOptimalApproach(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
