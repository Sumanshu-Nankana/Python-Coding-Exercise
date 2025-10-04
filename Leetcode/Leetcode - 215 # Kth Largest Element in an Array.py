import heapq

# Method:1 (Sorting)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# Method:1 (Using nlargest method of heapq)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]

# Method:2 (Using min-heap)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]