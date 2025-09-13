from typing import List


class Solution:
    def fourSumCountBruteForce(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        count = 0

        for i in range(0, n):
            for j in range(0, n):
                for k in range(0, n):
                    for l in range(0, n):
                        if (nums1[i] + nums2[j] + nums3[k] + nums4[l]) == 0:
                            count = count + 1

        return count

    def fourSumCountOptimalSolution(
        self, nums1: List[int], nums2: List[int], numm3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        hash_map = {}
        count = 0

        for i in range(0, n):
            for j in range(0, n):
                sum = nums1[i] + nums2[j]
                hash_map[sum] = hash_map.get(sum, 0) + 1

        for k in range(0, n):
            for l in range(0, n):
                sum = nums3[k] + nums4[l]
                remaining = 0 - sum
                if remaining in hash_map:
                    count = count + hash_map[remaining]

        return count


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

print(Solution().fourSumCountBruteForce(nums1, nums2, nums3, nums4))
print(Solution().fourSumCountOptimalSolution(nums1, nums2, nums3, nums4))
