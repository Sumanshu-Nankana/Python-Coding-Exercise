# using 2 hashmaps
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_hashmap = {}
        magazine_hashmap = {}

        for char in ransomNote:
            ransomNote_hashmap[char] = ransomNote_hashmap.get(char, 0) + 1

        for char in magazine:
            magazine_hashmap[char] = magazine_hashmap.get(char, 0) + 1

        for key, value in ransomNote_hashmap.items():
            if key not in magazine_hashmap or value > magazine_hashmap.get(key, 0):
                return False

        return True

# using 1 hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hashmap = {}

        for char in magazine:
            magazine_hashmap[char] = magazine_hashmap.get(char, 0) + 1

        for char in ransomNote:
            if char not in magazine_hashmap or magazine_hashmap.get(char, 0) == 0:
                return False
            magazine_hashmap[char] -= 1

        return True