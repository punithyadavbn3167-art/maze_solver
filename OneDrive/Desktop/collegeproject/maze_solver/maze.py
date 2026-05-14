# maze.py

maze = [
    ['S', 0, 1, 0],
    [0,   0, 1, 0],
    [1,   0, 0, 'G']
]

ROWS = len(maze)
COLS = len(maze[0])


def find_positions(maze):

    start = None
    goal = None

    for i in range(len(maze)):
        for j in range(len(maze[0])):

            if maze[i][j] == 'S':
                start = (i, j)

            if maze[i][j] == 'G':
                goal = (i, j)

    return start, goal


def get_neighbors(node, maze):

    directions = [
        (-1,0),  # up
        (1,0),   # down
        (0,-1),  # left
        (0,1)    # right
    ]

    neighbors = []

    for d in directions:

        x = node[0] + d[0]
        y = node[1] + d[1]

        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):

            if maze[x][y] != 1:
                neighbors.append((x,y))

    return neighbors