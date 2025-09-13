class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()

        rows = len(matrix)
        cols = len(matrix[0])

        # Find the rows and cols where zero exists
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set entire row to zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Set entire col to zero
        for i in range(rows):
            for j in zero_cols:
                matrix[i][j] = 0
