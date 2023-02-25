from typing import List


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumOptimalApproach(self, nums: List[int], target: int) -> List[int]:
            temp = {}
            n = len(nums)
            for i in range(0, n):
                diff = target - nums[i]
                if diff in temp:
                    return [temp[diff], i]
                else:
                    temp[nums[i]] = i



# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

nums = [3,3]
target = 6

print(Solution().twoSumBruteForce(nums, target))
print(Solution().twoSumOptimalApproach(nums, target))