from collections import defaultdict


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: Optional[TreeNode]) -> int:
        # Create the adjacency Matrix, (To Treat it as a Graph)
        # Because otherwise, it will be difficult to know - what is the PARENT node.
        adjacency_matrix = defaultdict(list)
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                adjacency_matrix[node.val].append(node.left.val)
                adjacency_matrix[node.left.val].append(node.val)

            if node.right:
                queue.append(node.right)
                adjacency_matrix[node.val].append(node.right.val)
                adjacency_matrix[node.right.val].append(node.val)

        # Now, just put start node in a queue
        # and check other nodes
        # and mark them as visited as we visited them
        visited = set()
        queue = [(start, 0)]
        visited.add(start)

        while len(queue) != 0:
            node, time = queue.pop(0)

            for neighbour in adjacency_matrix[node]:
                if neighbour not in visited:
                    queue.append((neighbour, time + 1))
                    visited.add(neighbour)

        return time


# We can also use DEQUE (it MIGHT increase a little but performance)

from collections import defaultdict
from collections import deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: Optional[TreeNode]) -> int:
        # Create the adjacency Matrix, (To Treat it as a Graph)
        # Because otherwise, it will be difficult to know - what is the PARENT node.
        adjacency_matrix = defaultdict(list)
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                adjacency_matrix[node.val].append(node.left.val)
                adjacency_matrix[node.left.val].append(node.val)

            if node.right:
                queue.append(node.right)
                adjacency_matrix[node.val].append(node.right.val)
                adjacency_matrix[node.right.val].append(node.val)

        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)

        while len(queue) != 0:
            node, time = queue.popleft()

            for neighbour in adjacency_matrix[node]:
                if neighbour not in visited:
                    queue.append((neighbour, time + 1))
                    visited.add(neighbour)

        return max_time
