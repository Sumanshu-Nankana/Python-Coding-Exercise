class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {j: set() for j in range(9)}
        box = {k: set() for k in range(9)}

        for i in range(9):
            for j in range(9):
                ele = board[i][j]

                if ele == ".":
                    continue

                # check whether element exists in row
                if ele in rows[i]:
                    return False
                rows[i].add(ele)

                # check whether element exists in column
                if ele in cols[j]:
                    return False
                cols[j].add(ele)

                # check whether element exists in grid
                # if we do not multiply by 3, we will always get either box 0, 1, 2
                # Thus we multiply by 3
                index = i // 3 * 3 + j // 3
                if ele in box[index]:
                    return False
                box[index].add(ele)

        return True