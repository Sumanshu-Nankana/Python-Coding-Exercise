from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort()
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left = left + 1
            boats = boats + 1
            right = right - 1
        return boats
