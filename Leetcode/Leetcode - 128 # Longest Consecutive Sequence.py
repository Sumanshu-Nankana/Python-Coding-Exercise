# Method -1
# All test cases passed
# But it is mentioned - we need to do in O(n)
# But as we are using Sorting - So it will take O(nlogn)

"""
Sort the list
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_length = 1
        current_length = 1

        for i in range(1, len(nums)):

            # Skip Duplicates values
            if nums[i] == nums[i-1]:
                continue

            # If the current element is equal to the previous element plus one, then
            # the current element is part of the current consecutive sequence.
            if nums[i] == nums[i-1]+1:
                current_length += 1
            else:
                longest_length = max(longest_length, current_length)

        # we need to check here for max (for array - where the consecutive sequence is at the end of the array)
        # Because in that case, it never comes to else condition
        # only current_length gets keep updated.
        return max(longest_length, current_length)


# Method-2
# We will use some extra space
# and Store all the elements in SET
# Because in SET - Lookup (i.e. Searching operation takes only O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest_length = 0

        # check for all elements
        for num in nums_set:
            # we will check the number if that is the start of the sequence
            # Because if there is any previous element also exists
            # It will cover in for loop - when it turns come

            # Though there is no need of IF-condition, but if we remove IF-condition
            # and check unnecessary - Then it will increase Time-Complexity
            # and there are chances many test cases might fail
            if num -1 not in nums_set:
                current_num = num
                current_length = 1

                # Now check whether consecutive elements of that current element exists or not
                # even though we are using IN operator here
                # But IN operator is on SET
                # which only take O(1)
                # That's why we used extra space
                # Because on Lists , IN operator takes O(n)
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1

                longest_length = max(longest_length, current_length)

        return longest_length
