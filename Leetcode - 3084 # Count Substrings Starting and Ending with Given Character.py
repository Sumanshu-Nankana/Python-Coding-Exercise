#Method-1
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        m = s.count(c)
        return int(m * (m+1)/2)


#Method-2
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        total_count = 0
        past_count = 0

        for ch in s:
            if ch == c:
                total_count = total_count + 1 + past_count
                past_count += 1

        return total_count