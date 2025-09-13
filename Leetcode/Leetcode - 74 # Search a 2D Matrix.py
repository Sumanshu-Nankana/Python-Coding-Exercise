# Solution-1
# Check which row target element is and then apply Binary Search in that particular row
# Time complexity m*log(n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of cols

        for row in range(m):
            # if element is in a row
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                # Perform Binary Search
                left = 0
                right = n - 1

                while left <= right:
                    mid = (left + right) // 2

                    if matrix[row][mid] == target:
                        return True

                    elif matrix[row][mid] < target:
                        left = mid + 1

                    else:
                        right = mid - 1
        return False


# Solution-2
# In above solution, we are checking all rows
# we know all rows are also Sorted
# So we can apply Binary Search in Rows as well, to find the exact row
# Then apply Binary Search in that row (to find target) - same as above.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # no of rows
        n = len(matrix[0])  # no of cols

        top = 0
        bottom = m - 1

        # find the row in which our element exists

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # Apply Binary search on that row

        row = (top + bottom) // 2
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False