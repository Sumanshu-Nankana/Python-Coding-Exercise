from typing import List


class Solution:
    def __init__(self):
        pass

    def singleNumberBruteForce(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            temp[i] = temp.get(i, 0) + 1

        for key, value in temp.items():
            if value == 1:
                return key


    def singleNumberFirstOptimal(self, nums: List[int]) -> int:
        temp_set = set(nums)
        return 2*sum(temp_set) - sum(nums)



    def singleNumberSecondOptimal(self, nums: List[int]) -> int:
        n, r = len(nums), nums[0]
        for i in range(1, n):
            r = r ^ nums[i]
        return r



nums = [4, 1, 2, 1, 2]
print(Solution().singleNumberBruteForce(nums))
print(Solution().singleNumberFirstOptimal(nums))
print(Solution().singleNumberSecondOptimal(nums))
