class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for index, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = index
            else:
                previous_index = index_map[num]
                current_index = index
                difference = abs(previous_index - current_index)
                if difference <= k:
                    return True
                else:
                    index_map[num] = current_index
        return False