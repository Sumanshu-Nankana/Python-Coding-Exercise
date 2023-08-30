class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        n, start, tank = len(gas), 0, 0

        for i in range(n):
            tank = tank + gas[i]
            distance = cost[i]
            tank = tank - distance

            if tank < 0:
                start = i + 1
                tank = 0

        return start


