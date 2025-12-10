# Bubble Sort
"""
First-Pass : Move the Highest Number to End
Second-Pass: Move the Second Highest Number to Second Last
..
..
so on..

nums = [9, 8, 8, 1, 2]
first-pass (Loop from 0 to end) = [8, 8, 1, 2, 9]
second-pass (Loop from 0 to end-1) = [8, 1, 2, 8, 9]
third-pass (loop from 0 to end-2) = [1, 2, 8, 8, 9]
..
so on..

Time Complexity:
Best: O(n^2)
Worst: O(n^2)
Space: O(1)
"""
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] >= nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums

# Selection Sort
"""
First-Pass (o to n) - We will first find the smallest element and swap it with the first element
Second-Pass (1 to n) - Again Find the Smallest element and swap it with the second element
Third Pass (2 to n) - Find the Smallest element and swap it with the third element


Basically,
Loop-1 : Find minimum element from 0 to n, then swap with first place (which means now minium is on front or index-0)
Loop-2 : Find minimum element from 1 to n (as index 0 is already filled with minimum). Then swap with first place (which means now 2nd minimum is on front or index-1)
and so on....

nums = [9, 8, 8, 1, 2]

First-Pass : [1, 8, 8, 9, 2]
Second-Pass: [1, 2, 8, 9, 8]
Third-Pass: [1, 2, 8, 9, 8]
Fourth Pass: [1, 2, 8, 8, 9]
"""
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums


# Merge Sort
"""
Divide and Conquer Algorithm

- Divide the array into two halves
- Recursively sort each half
- Merge the sorted half back together

example
nums = [7, 3, 2, 16, 24, 4, 11, 9]
- Divide the array into two halves
- [7, 3, 2, 16] and [24, 4, 11, 9]
- Continue Splitting, until each just contains one element
- [7, 3] [2, 16] and [24, 4,] [11, 9]
- [7], [3], [2], [16] and [24], [4], [11], [9]
- Merge these single elements into Pairs
- [3, 7] [2, 16] and [4, 24] [9, 11]
- Continue Merging pairs into Larger Sorting sorted aaray
- [2, 3, 7, 16] and [4, 9, 11, 24]
- Finally merge the two sorted haves
- [2, 3, 4, 7, 9, 11, 16, 24]

"""

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self._mergeSort(nums)
        return nums

    def _mergeSort(self, nums):
        # Stop Dividing when the list length is 1 or less
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]  # elements from 0 to min-1
            right = nums[mid:] # elements from mid to the end

            self._mergeSort(left)
            self._mergeSort(right)

            self._merge(nums, left, right)

    def _merge(self, nums, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Append any remaining elements from the left list
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # Append any remaining elements from the right list
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

nums = [9, 8, 8, 1, 2]
s = Solution()
print(s.sortArray(nums))