# Using Brute Force Approach
# 18 / 21 testcases passed
# Time Limit Exceeded Error


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        n = len(nums)

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum = current_sum + nums[j]
                if current_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break

        if min_length != float("inf"):
            return min_length
        else:
            return 0


# Using the Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        min_length = float("inf")
        current_sum = 0

        while right < n:
            current_sum = current_sum + nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum = current_sum - nums[left]
                left = left + 1
            right = right + 1

        if min_length != float("inf"):
            return min_length
        else:
            return 0
