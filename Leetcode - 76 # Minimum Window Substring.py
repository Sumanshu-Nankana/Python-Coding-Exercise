from collections import Counter

# 231 Test cases Passed out of 267
class Solution:
    def minWindowBruteForceMethodUsingHelper(self, s: str, t: str) -> str:
        min_length = float("inf")
        min_string = ""
        n = len(s)
        hash_map_t = Counter(t)
        if len(t) > len(s): return min_string
        for i in range(n):
            for j in range(i, n):
                window = s[i:j+1]
                flag = self.is_window_valid(window, t)
                if flag and len(window) < min_length:
                    min_length = len(window)
                    min_string = window
        return min_string


    def is_window_valid(self, window: str, t: str) -> bool:
        hash_map_t = Counter(t)
        hash_map_window = Counter(window)

        for key in hash_map_t.keys():
            if hash_map_window[key] < hash_map_t[key]:
                return False
        return True




# 265 Test Cases Passed out of 267
from typing import Dict

class Solution:
    def is_valid_substring(self, substring: str, hash_map_t: Dict[str, int]) -> bool:
        hash_map_substring = Counter(substring)
        if len(hash_map_t) > len(substring): return False
        for key in hash_map_t.keys():
            if hash_map_t[key] > hash_map_substring[key]:
                return False
        return True

    def minWindowOptimalMethod1(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        left, right = 0, 0
        min_length, min_string = float("inf"), ""
        n = len(s)
        hash_map_t = Counter(t)
        while left <= right and right < n:
            substring = s[left:right + 1]
            if not self.is_valid_substring(substring, hash_map_t):
                right = right + 1
            else:
                substring_len = len(substring)
                if substring_len < min_length:
                    min_length = substring_len
                    min_string = substring
                left = left + 1
        return min_string




# All Test Cases Passed
# Approach is Same - But Instead of again counting for hash_map,
# we are storing, and removing and adding current element

from collections import defaultdict
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        min_length, min_string = float("inf"), ""
        hash_map_t = Counter(t)
        n = len(s)
        counter_search = {}
        count = 0

        while right < n:
            counter_search[s[right]] = counter_search.get(s[right], 0) + 1
            if s[right] in hash_map_t:
                if counter_search[s[right]] <= hash_map_t[s[right]]:
                    count = count + 1

            while left <= right and count == len(t):
                if min_length > right - left + 1:
                    min_length = right - left + 1
                    min_string = s[left: right + 1]

                counter_search[s[left]] = counter_search.get(s[left], 0) - 1
                if s[left] in hash_map_t and counter_search[s[left]] < hash_map_t[s[left]]:
                    count = count - 1

                left = left + 1

            right = right + 1

        return min_string


s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.minWindowBruteForceMethod(s, t))
obj = Solution1()
print(obj.minWindowOptimalMethod1(s, t))
obj = Solution2()
print(obj.minWindow(s, t))
