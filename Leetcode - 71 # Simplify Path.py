class Solution:
    def simplifyPath(self, path: str) -> str:
        output = ""
        stack = []
        tokens = path.split("/")
        for token in tokens:
            if token == '' or token == '.':
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)

        canonical_path = "/" + "/".join(stack)
        return canonical_path