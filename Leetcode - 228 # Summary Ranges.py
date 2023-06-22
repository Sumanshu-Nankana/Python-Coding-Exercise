class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        n = len(nums)

        if len(nums) == 0: return []
        start = nums[0]
        end = nums[0]

        for i in range(1, n):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start) + '->' + str(end))
                start = end = nums[i]

        if start == end:
            output.append(str(start))
        else:
            output.append(str(start) + '->' + str(end))
        return output