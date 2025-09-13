from typing import List


class Solution:
    def searchRangeBruteForceMethod(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        n = len(nums)
        for i in range(0, n):
            if nums[i] == target:
                first = i
                break

        for j in range(n - 1, -1, -1):
            if nums[j] == target:
                last = j
                break

        return [first, last]

    def searchRangeOptimalMethod(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # Logic to find the First Position
        left, right = 0, n - 1
        first, last = -1, -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid - 1] != target or mid == 0:
                    first = mid
                    break
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # Logic to find the Last Position
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid + 1 < n and nums[mid + 1] != target or mid == n - 1:
                    last = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [first, last]


nums = [5, 7, 7, 8, 8, 10]
target = 6
print(Solution().searchRangeBruteForceMethod(nums, target))
print(Solution().searchRangeOptimalMethod(nums, target))
