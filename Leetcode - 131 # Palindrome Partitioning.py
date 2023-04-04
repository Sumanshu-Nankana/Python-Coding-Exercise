def is_palindrome(prefix):
    return prefix == prefix[::-1]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []

        # when there is nothing, we need to return List of List
        if s == "":
            return [[]]

        for i in range(len(s)):
            prefix = s[:i+1]
            if is_palindrome(prefix):
                suffix_partitions = self.partition(s[i+1:])
                # Because we are returning list of List, so, to append we need to run a loop to pick the element
                for partition in suffix_partitions:
                    partitions.append([prefix] + partition)

        return partitions