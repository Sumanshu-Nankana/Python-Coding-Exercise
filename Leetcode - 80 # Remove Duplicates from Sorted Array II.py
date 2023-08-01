# We are going to place the elements at its correct position
# "i" is the place where we need to place the element
# We will run the loop
# if element is not correct or more than -2, skip that
# as soon as we found correct element, we will place it at correct position.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i




