from typing import List


class Solution:
    def missingNumberBruteForceMethod(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                break
        return i



    def missingNumberSecondMethod(self, nums: List[int]) -> int:
        numbers = {}
        for i in nums:
            numbers[i] = True

        n = len(nums)
        for i in range(0, n+1):
            if i not in numbers:
                break
        return i


    def missingNumberOptimalApproach(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1) // 2

        for num in nums:
            total = total - num

        return total


nums = [1, 2]
print(Solution().missingNumberBruteForceMethod(nums))
print(Solution().missingNumberSecondMethod(nums))
print(Solution().missingNumberOptimalApproach(nums))