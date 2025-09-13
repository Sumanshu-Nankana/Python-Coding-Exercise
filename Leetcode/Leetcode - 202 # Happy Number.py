class Solution:
    def sumDigitsSquare(self, n):
        digit_sq_sum = 0
        while n != 0:
            n, digit = divmod(n, 10)
            digit_sq_sum = digit_sq_sum + digit**2

        return digit_sq_sum

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumDigitsSquare(n)
            if n == 1:
                return True
        return False
