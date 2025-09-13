class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        for key, value in s_dict.items():
            if t_dict.get(key, 0) != value:
                return False

        return True


# using one dictionary
class Solution:
    def isAnagram(self, s, t) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            s_dict[char] = s_dict.get(char, 0) - 1
            if s_dict[char] < 0:
                return False

        return True
