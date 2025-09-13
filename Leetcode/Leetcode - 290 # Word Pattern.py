class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split()
        pattern_to_s = {}
        s_to_pattern = {}

        if len(pattern) != len(list_s):
            return False

        for char, word in zip(pattern, list_s):
            if char in pattern_to_s and pattern_to_s[char] != word:
                return False
            if word in s_to_pattern and s_to_pattern[word] != char:
                return False
            pattern_to_s[char] = word
            s_to_pattern[word] = char
        return True
