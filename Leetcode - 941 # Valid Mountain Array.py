from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)

        i = 1
        while i < length and arr[i] > arr[i - 1]:
            i = i + 1

        if i == 1 or i == length:
            return False

        while i < length and arr[i] < arr[i - 1]:
            i = i + 1

        if i == length:
            return True
