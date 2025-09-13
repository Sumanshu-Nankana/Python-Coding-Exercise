class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for m in moves:
            if m == "U":
                y = y + 1
            elif m == "D":
                y = y - 1
            elif m == "L":
                x = x - 1
            else:
                x = x + 1

        return x == 0 and y == 0


moves = "LL"
print(Solution().judgeCircle(moves))
