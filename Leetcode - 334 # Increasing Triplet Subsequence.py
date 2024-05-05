# Naive Approach
# O(n^3) - Time Complexity (checking all possible triplets)
# 76 / 84 testcases passed
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        for i in range(n - 2):
            for j in range(i+1, n-1):
                if nums[j] > nums[i]:
                    for k in range(j+1, n):
                        if nums[k] > nums[j]:
                            return True

        return False

# O(n) - Time Complexity
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        num1, num2 = float('inf'), float('inf')

        for num3 in nums:
            if num3 <= num1:
                num1 = num3
            elif num3 <= num2:
                num2 = num3
            else:
                return True

        return False