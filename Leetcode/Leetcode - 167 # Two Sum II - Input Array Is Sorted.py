# Solve using Two Pointer Approach
# O(n) and without using extra space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right = right - 1
            else:
                left = left + 1


# O(n) and with using extra space
# we will store element in hash_map with index
# and we will scan elements and check if remaning element (target-num) exists in dictionary or not.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement] + 1, index + 1]

            hash_map[num] = index
