from typing import List


class Solution(object):
    def maximumSumSubarrayBruteForceMethod(self, Arr: List[int], K: int) -> int:
        r = len(Arr) - K + 1
        max_sum = float('-inf')
        for i in range(r):
            current_sum = 0
            for j in range(i, i+K):
                current_sum = current_sum + Arr[j]
            max_sum = max(max_sum, current_sum)
        return max_sum

    def maximumSumSubarraySlidingMethod(self, Arr: List[int], K: int) -> int:

        window_sum = 0
        for i in range(K):
            window_sum = window_sum + Arr[i]

        max_sum = window_sum
        i = 1
        r = len(Arr) - K + 1

        while i < r:
            window_sum = window_sum - Arr[i-1] + Arr[i+K-1]
            max_sum = max(window_sum, max_sum)
            i = i + 1
        return max_sum

        # We can use the For Loop as well, instead of while Loop
        # r = len(Arr) - K
        # for i in range(r):
        #     window_sum = window_sum - Arr[i] + Arr[i+K]
        #     max_sum = max(window_sum, max_sum)
        # return max_sum



Arr = [10, -20, 30, 40, 50, -60, 70, 9, 18, -5, 6]
K = 4
print(Solution().maximumSumSubarrayBruteForceMethod(Arr, K))
print(Solution().maximumSumSubarraySlidingMethod(Arr, K))