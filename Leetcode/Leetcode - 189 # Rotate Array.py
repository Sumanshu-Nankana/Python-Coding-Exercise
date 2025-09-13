class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Get the effective number of rotations
        k = k % len(nums)

        # reverse the entire list
        nums.reverse()

        # reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)

    @staticmethod
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
