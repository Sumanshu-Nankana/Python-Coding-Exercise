class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        output = [[] for _ in range(numRows)]
        row = 0

        for char in s:
            output[row].append(char)
            if row == 0:
                increment = True
            elif row == numRows - 1:
                increment = False

            if increment:
                row += 1
            else:
                row -= 1

        zigzag_string = ""
        for row in output:
            for char in row:
                zigzag_string = zigzag_string + char

        return zigzag_string
