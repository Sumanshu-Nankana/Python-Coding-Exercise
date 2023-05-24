# using inbuilt function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # find and index methods are same
        # difference is find return -1, if string not found
        # index will return error
        return haystack.find(needle)


# without using inbuilt function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        if haystack_length < needle_lengthz:
            return -1

        i = 0

        while i <= (haystack_length - needle_length):
            if haystack[i:needle_length + i] == needle:
                return i
            else:
                i = i + 1

        return -1
