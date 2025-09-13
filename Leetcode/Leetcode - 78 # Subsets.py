from typing import List


class Solution(object):
    def subsets(self, nums):
        output = [[]]
        if len(nums) == 0:
            return output

        for num in nums:
            n = len(output)
            for i in range(n):
                r = output[i] + [num]
                output.append(r)

        return output


# Same approach - Just using List Comprehension
class Solution(object):
    def subsets(self, nums):
        output = [[]]

        for num in nums:
            output = output + [ele + [num] for ele in output]
        return output
