# dijkstra_solver.py

import heapq
from maze import get_neighbors


def dijkstra(maze, start, goal):

    pq = []
    heapq.heappush(pq, (0, start))

    distance = {start:0}
    parent = {}

    while pq:

        current_cost, node = heapq.heappop(pq)

        if node == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in get_neighbors(node, maze):

            new_cost = current_cost + 1

            if neighbor not in distance or new_cost < distance[neighbor]:

                distance[neighbor] = new_cost
                parent[neighbor] = node

                heapq.heappush(pq, (new_cost, neighbor))

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