from itertools import combination


# Approach-1 (O(n^2))
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        words_length = len(words)
        count = 0

        for i in range(words_length - 1):
            for j in range(i + 1, words_length):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count

# Approach-2, using itertools to get the list of combinations
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        words_combination = list(combinations(words, 2))
        count = 0

        for i in words_combination:
                if i[1].startswith(i[0]) and i[1].endswith(i[0]):
                    count += 1
        return count