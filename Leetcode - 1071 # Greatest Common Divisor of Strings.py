class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def is_divided(prefix, string):
            return string == prefix * (len(string) // len(prefix))

        result = ""

        len1, len2 = len(str1), len(str2)
        max_prefix_length = min(len1, len2)
        # Try All Prefixes of any string,
        # But better to try for string which is of small length, So that we try less iteration
        for i in range(max_prefix_length):
            prefix = str1[:i + 1]
            if is_divided(prefix, str1) and is_divided(prefix, str2):
                result = prefix

        return result

# The another best approach is to start from highest length of prefix
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def is_divided(prefix, string):
            return string == prefix * (len(string) // len(prefix))

        result = ""

        len1, len2 = len(str1), len(str2)
        max_prefix_length = min(len1, len2)

        # Starting from maximum prefix length and then decrementing
        for i in range(max_prefix_length, 0, -1):
            prefix = str1[:i]
            if is_divided(prefix, str1) and is_divided(prefix, str2):
                result = prefix
                break  # Once found the largest divisor, no need to continue

        return result
