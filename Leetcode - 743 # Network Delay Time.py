from collections import defaultdict


class Solution:
    def bfs(self, adj_list, start_node, total_nodes):
        delay_array = [0] + [float("inf")] * total_nodes
        queue = [(start_node, 0)]

        while queue:
            node, time = queue.pop(0)
            if time < delay_array[node]:
                delay_array[node] = time

                for next_node, next_time in adj_list[node]:
                    queue.append((next_node, time + next_time))

        if max(delay_array) < float("inf"):
            return max(delay_array)
        else:
            return -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for item in times:
            adj_list[item[0]].append((item[1], item[2]))

        minimum_delay_time = self.bfs(adj_list, k, n)
        return minimum_delay_time
