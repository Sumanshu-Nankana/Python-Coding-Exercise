class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        reverse_s = s[::-1]

        for i in range(n - 1):
            substring = s[i:i + 2]
            if substring in reverse_s:
                return True

        return False


