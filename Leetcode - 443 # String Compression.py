class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0

        while right < len(chars):
            current_char = chars[right]
            count = 1
            while right < len(chars) - 1 and chars[right + 1] == current_char:
                right += 1
                count += 1

            chars[left] = current_char
            left += 1

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1

            right += 1

        return left