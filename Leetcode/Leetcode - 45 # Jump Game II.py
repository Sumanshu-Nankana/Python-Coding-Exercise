# We are going to check all possibilities
# where we can reach farthest
# And we will increment jump variable,
# when we know the index from which we can reach farthest i.e. after checking all conditions
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        # Farthest index that can be reached with current jumps
        current_end = 0
        farthest = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])

            if current >= len(nums) - 1:
                break

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
