class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        output.append(intervals[0])

        for current in intervals[1:]:

            last = output[-1]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                output.append(current)

        return output



# intervals =  [[1,3],[2,6],[8,10],[15,18]]
#intervals =  [[1,4],[4,5]]
intervals =  [[4,7],[1,4]]

s = Solution()
output = s.merge(intervals=intervals)
print(output)