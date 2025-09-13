from typing import List
from collections import Counter


class Solution:
    def majorityElementUsingExtraSpace(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        for n in nums:
            if hash_map[n] > len(nums) // 2:
                return n

    def majorityElementUsingExtraSpace1(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        n = len(nums)
        for k, v in hash_map.items():
            if v > n / 2:
                return k

    def majorityElementUsingCounter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = Counter(nums)
        for k, v in nums.items():
            if v > n / 2:
                return k

    def majorityElementWithoutExtraSpace(self, nums: List[int]) -> int:
        # using Boyer–Moore_majority_vote_algorithm
        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        result, count = 0, 0
        for num in nums:
            if count == 0:
                result = num

            if result == num:
                count = count + 1
            else:
                count = count - 1

        return result


# nums = [3,2,3]
nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElementUsingExtraSpace(nums))
print(Solution().majorityElementUsingExtraSpace1(nums))
print(Solution().majorityElementUsingCounter(nums))
print(Solution().majorityElementWithoutExtraSpace(nums))
