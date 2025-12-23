class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[b] != top_element:
                    return False
            else:
                stack.append(b)

        return not stack