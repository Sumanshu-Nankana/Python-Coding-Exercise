class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for start, stop in points:
            if start > end:
                arrows += 1
                end = stop

        return arrows
