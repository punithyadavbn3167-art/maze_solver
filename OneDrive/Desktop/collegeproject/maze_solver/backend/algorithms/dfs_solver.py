from maze import get_neighbors

def dfs(maze, start, goal):

    stack = [start]
    visited = set()
    parent = {}

    while stack:

        node = stack.pop()

        if node == goal:
            return reconstruct_path(parent, start, goal)

        if node not in visited:

            visited.add(node)

            for neighbor in get_neighbors(node, maze):

                if neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)

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