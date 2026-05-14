# bfs_solver.py

from collections import deque
from maze import get_neighbors

def bfs(maze, start, goal):

    queue = deque([start])
    visited = set()
    parent = {}

    while queue:

        node = queue.popleft()

        if node == goal:
            return reconstruct_path(parent, start, goal)

        if node not in visited:

            visited.add(node)

            for neighbor in get_neighbors(node, maze):

                if neighbor not in visited:
                    parent[neighbor] = node
                    queue.append(neighbor)

    return None


def reconstruct_path(parent, start, goal):

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path