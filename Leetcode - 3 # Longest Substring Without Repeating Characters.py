class Solution:
    def lengthOfLongestSubstringBrueForceMethod(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        n = len(s)
        max_length = 0
        for i in range(0, n):
            length = 1
            temp = {}
            temp[s[i]] = 1
            for j in range(i + 1, n):
                if temp.get(s[j]) is None:
                    length = length + 1
                    temp[s[j]] = 1
                else:
                    break
            max_length = max(length, max_length)
        return max_length


    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1: return len(s)
        L = 0
        R = 0
        n = len(s)
        seenElements = {}
        max_length = 0
        while L < n and R < n:
            currentElement = s[R]
            if currentElement not in seenElements:
                seenElements[currentElement] = R
            else:
                prev_loc = seenElements[currentElement]
                L = max(L, prev_loc + 1)
                seenElements[currentElement] = R
            R = R + 1
            max_length = max(max_length, R-L)
        return max_length




s = "abba"
print(Solution().lengthOfLongestSubstringBrueForceMethod(s))
print(Solution().lengthOfLongestSubstring(s))
