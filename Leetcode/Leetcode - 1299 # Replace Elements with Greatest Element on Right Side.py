# Time Limit Exceeded


# Updating from Start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n - 1):
            arr[i] = max(arr[i + 1 :])

        arr[n - 1] = -1

        return arr


# Accepted Solution
# Updating from End
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1

        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(temp, max_right)

        return arr
