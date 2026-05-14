import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from maze import maze, find_positions, get_neighbors


def animate_solver(maze):

    start, goal = find_positions(maze)

    queue = deque([start])
    visited = set()

    grid = np.array([[0 if c != 1 else 1 for c in row] for row in maze])

    plt.ion()
    fig, ax = plt.subplots()

    while queue:

        node = queue.popleft()

        if node == goal:
            break

        if node not in visited:

            visited.add(node)

            x, y = node
            grid[x][y] = 0.5  # visited node color

            ax.clear()
            ax.imshow(grid, cmap="viridis")
            plt.pause(0.3)

            for neighbor in get_neighbors(node, maze):
                queue.append(neighbor)

    plt.ioff()
    plt.show()


animate_solver(maze)