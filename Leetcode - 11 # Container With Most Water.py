from typing import List


class Solution:
    def maxAreaBruteForceMethod(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for i in range(0, length-1):
            for j in range(i+1, length):
                h = min(height[i], height[j])
                w = j - i
                area = w * h
                max_area = max(max_area, area)
        return max_area

    def maxAreaOptimalMethod(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxAreaBruteForceMethod(height))
print(Solution().maxAreaOptimalMethod(height))
