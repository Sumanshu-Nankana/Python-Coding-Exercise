class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on end key
        points.sort(key=lambda x: x[1])

        # Atleast one arrow is required
        arrows = 1
        end = points[0][1]

        # Update the remaining points (as no need to check for first point)
        points = points[1:]

        # if start of balloon does not comes in range (less than end of previous) of earlier balloon then increment arrows
        for start, stop in points:
            if start > end:
                arrows += 1
                end = stop

        return arrows
