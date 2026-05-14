from backend.algorithms.astar_solver import astar
from backend.algorithms.bfs_solver import bfs
from backend.algorithms.dfs_solver import dfs
from backend.algorithms.dijkstra_solver import dijkstra


def solve_maze(maze, start, goal, algorithm):

    start = tuple(start)
    goal = tuple(goal)

    if algorithm == "astar":
        path = astar(maze, start, goal)

    elif algorithm == "bfs":
        path = bfs(maze, start, goal)

    elif algorithm == "dfs":
        path = dfs(maze, start, goal)

    elif algorithm == "dijkstra":
        path = dijkstra(maze, start, goal)

    else:
        raise ValueError("Unknown algorithm")

    if path is None:
        return []

    return [list(p) for p in path]