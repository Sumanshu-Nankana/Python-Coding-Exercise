class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while left<=right and top<=bottom:
            # Traverse Top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top = top + 1

            # Traverse Rightmost column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right = right - 1

            # Check if there are more rows and columns to traverse
            if top <= bottom and left <= right:
                # Traverse Bottom Row
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom = bottom - 1

                #Traverse Left Row
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left = left + 1

        return result