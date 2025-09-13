class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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