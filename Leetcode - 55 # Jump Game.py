# our main goal is to reach at last index
# So, from all index, we will check where we can reach MAX
# if from any index, we reach far, we wil update our reachable variable
# if at any index, reachable is previous index
# It means, we can't move further, So, Return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i > reachable:
                return False
            reachable = max(reachable, i + num)
            if reachable == n - 1:
                return True

        return True