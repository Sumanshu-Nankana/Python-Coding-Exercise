from typing import List


class Solution:
    def moveZeroesBruteForceMethod(self, nums: List[int]) -> List[int]:
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


    def moveZerosTwoPointersAnotherApproach(self, nums: List[int]) -> None:
        i = 0
        for j in nums:
            if j != 0:
                nums[i] = j
                i = i + 1

        for x in range(i, len(nums)):
            nums[x] = 0
