class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        number_of_islands = 0
        visited = set()

        def check_current_island(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))
            check_current_island(row + 1, col)
            check_current_island(row - 1, col)
            check_current_island(row, col + 1)
            check_current_island(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    check_current_island(i, j)
                    number_of_islands += 1

        return number_of_islands


# No Extra Memory - Method-2
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, columns = len(grid), len(grid[0])

        count = 0

        def check_current_island(r, c):

            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            check_current_island(r, c + 1)
            check_current_island(r, c - 1)
            check_current_island(r + 1, c)
            check_current_island(r - 1, c)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    check_current_island(r, c)
                    count += 1

        return count


