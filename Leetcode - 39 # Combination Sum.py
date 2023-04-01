from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        temp = []
        candidates = list(set(candidates))
        self.findCombination(candidates, target, output, temp, 0)
        return output

    def findCombination(self, candidates, target, output, temp, idx):

        # Base Case
        if target == 0:
            output.append(list(temp))

        for i in range(idx, len(candidates)):
            if target - candidates[i] >= 0:
                temp.append(candidates[i])
                self.findCombination(candidates, target-candidates[i], output, temp, i)
                temp.remove(candidates[i])
