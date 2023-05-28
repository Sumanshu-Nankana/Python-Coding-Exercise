from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # create a frequency counter
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        # Sort the num_count Based on Frequency (In Increasing Order)
        # if Frequency is Same (Then Sort Based on Key - in Decreasing Order)
        sorted_num_count = dict(sorted(num_count.items(), key=lambda x: (x[1], -x[0])))

        # Create the result array
        nums = []
        for key, count in sorted_num_count.items():
            nums += [key] * count  # this is just like adding two lists

        return nums


# nums = [1, 1, 2, 2, 2, 3]
# nums = [2, 3, 1, 3, 2]
# nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
s = Solution()
s.frequencySort(nums)
