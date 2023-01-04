from typing import List


class Solution:
    def moveZeroesBruteForceMethod(self, nums: List[int]) -> None:
        output = []
        for i in nums:
            if i != 0:
                output.append(i)

        n = len(nums) - len(output)

        for _ in range(n):
            output.append(0)

        return output


    def moveZerosTwoPointers(self, nums: List[int]) -> None:
        left, right = 0, 0

        while left <= right and right < len(nums):
            if nums[left] == 0 and nums[right] == 0:
                right = right + 1
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
            else:
                left = left + 1
                right = right + 1

        return nums

    def moveZerosTwoPointersAnotherApproach(self, nums: List[int]) -> None:
        i = 0
        for j in nums:
            if j != 0:
                nums[i] = j
                i = i + 1

        for x in range(i, len(nums)):
            nums[x] = 0

        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroesBruteForceMethod(nums))
nums = [0, 1, 0, 3, 12]
print(Solution().moveZerosTwoPointers(nums))
nums = [0, 1, 0, 3, 12]
print(Solution().moveZerosTwoPointersAnotherApproach(nums))
