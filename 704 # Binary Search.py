from typing import List


class Solution(object):
    def linear_search(self, nums: List[int], target: int) -> int:
        for ix, i in enumerate(nums):
            if target == i:
                return ix
        return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 0
linear_result = Solution().linear_search(nums, target)
binary_result = Solution().binary_search(nums, target)

if binary_result != -1:
    print(f"{target} found in {nums} at index {linear_result}")
else:
    print(f"{target} not found in {nums}")

