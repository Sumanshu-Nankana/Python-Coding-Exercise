from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        x_map = defaultdict(set)
        y_map = defaultdict(set)

        # [[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]]
        for x, y in buildings:
            x_map[x].add(y)  # x_map: {2: {4, 3, 2}, 1: {2, 4, 3}, 3: {1, 3}}
            y_map[y].add(x)  # y_map: {4: {2, 1}, 2: {1, 2}, 1: {3}, 3: {2, 3, 1},

        # Min/Max Y for a given X (Left/Right Boundaries)
        min_x_map = {x: min(ys) for x, ys in x_map.items()}  # min_x_map: {2: 2, 1: 2, 3: 1}
        max_x_map = {x: max(ys) for x, ys in x_map.items()}  # max_x_map: {2: 4, 1: 4, 3: 3}


        # Min/Max X for a given Y (Top/Bottom Boundaries)
        min_y_map = {y: min(xs) for y, xs in y_map.items()} # min_y_map: {4: 1, 2: 1, 1: 3, 3: 1}
        max_y_map = {y: max(xs) for y, xs in y_map.items()} # max_y_map: {4: 2, 2: 2, 1: 3, 3: 3}


        count = 0
        for x, y in buildings:

            is_covered_by_left = x > min_y_map.get(y)

            is_covered_by_right = x < max_y_map.get(y)


            is_covered_by_top = y < max_x_map.get(x)

            is_covered_by_bottom = y > min_x_map.get(x)

            if is_covered_by_left and is_covered_by_right and is_covered_by_top and is_covered_by_bottom:
                count += 1

        return count



s = Solution()
# n = 3
# buildings = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]

#n = 3
#buildings = [[1,1],[1,2],[2,1],[2,2]]

#n = 5
#buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

n = 4
buildings = [[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]]

print(s.countCoveredBuildings(n, buildings))