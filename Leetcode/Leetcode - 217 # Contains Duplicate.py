from typing import List


class Solution:
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicateSecondMethod(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) > len(nums_set):
            return True
        else:
            return False

    def containsDuplicateThirdMethod(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map[i] = 1
        return False

    def containsDuplicateFourthMethod(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) <= 1:
            return False

        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


nums = [1, 2, 3, 1]  #
# nums = [1,2,3,4]
print(Solution().containsDuplicateBruteForce(nums))
print(Solution().containsDuplicateSecondMethod(nums))
print(Solution().containsDuplicateThirdMethod(nums))
print(Solution().containsDuplicateFourthMethod(nums))
