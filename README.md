Maze Solver – AI-Based Pathfinding Web Application

An interactive, web-based Maze Solver application that implements and visualizes AI search algorithms to find paths through dynamically generated mazes. Users can generate mazes, place obstacles, visualize path traversal in real time, and compare the performance of different pathfinding algorithms.

 Features

- **Dynamic Maze Generation:** Generate mazes with different layouts.
- **Obstacle Placement:** Add obstacles and control the maze environment.
- **Path Visualization:** Visualize the exploration process and final path in real time.
- **Multiple Search Algorithms:** Supports BFS, DFS, Dijkstra's, and A*.
- **Algorithm Comparison:** Compare pathfinding behavior and results across algorithms.
- **Shortest Path Detection:** Identify optimal paths using suitable search algorithms.
- **Interactive Web Interface:** Simple and user-friendly interface for maze exploration.

 Algorithms Implemented

| Algorithm | Description |
|---|---|
| BFS | Explores nodes level by level to find the shortest path in an unweighted maze. |
| DFS | Explores one path deeply before backtracking. |
| Dijkstra's Algorithm | Finds the shortest path using cumulative path costs. |
| A* Search | Uses path cost and heuristic estimation to guide the search efficiently. |

Tech Stack

**Frontend**
- React.js
- JavaScript
- CSS
- React Router

**Backend**
- Python
- FastAPI
- Uvicorn

**Libraries**
- NumPy
- Matplotlib

 System Architecture

1. **Frontend (React.js):** Provides the interactive maze interface, controls, and visualization.
2. **Backend (FastAPI):** Handles API requests and pathfinding operations.
3. **Algorithm Engine:** Executes BFS, DFS, Dijkstra's, and A* algorithms.
4. **Visualization:** Displays maze exploration, obstacles, and the resulting path.

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd maze-solver
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend API:
`http://127.0.0.1:8000`

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm start
```

Open the local frontend URL displayed in your terminal.

*Note: Adjust the directory names and startup commands according to your actual project structure.*

Algorithm Performance

The application allows users to compare the pathfinding behavior of different algorithms.

- **BFS:** Guarantees the shortest path in an unweighted maze.
- **DFS:** Finds a path but does not guarantee the shortest path.
- **Dijkstra's:** Guarantees the shortest path when edge weights are non-negative.
- **A*:** Uses heuristic-based search to efficiently find an optimal path when the heuristic is appropriate.

In the implemented test scenarios, A* demonstrated efficient pathfinding performance while maintaining optimal path results.

 Project Objectives

- Understand and implement fundamental AI search algorithms.
- Explore heuristic-based and uninformed search strategies.
- Visualize graph traversal and pathfinding techniques.
- Integrate a React frontend with a Python FastAPI backend.
- Compare algorithm behavior in interactive environments.

 Project Information

- **Project Name:** Maze Solver
- **Project Type:** Mini Project
- **Domain:** Artificial Intelligence & Machine Learning
- **Academic Year:** 2025–2026
- **Role:** Full Stack Development & AI Algorithm Implementation

 Future Enhancements

- Add additional pathfinding algorithms.
- Introduce weighted mazes and custom terrain costs.
- Display execution time and nodes explored.
- Add maze-solving animations and performance charts.
- Support custom maze dimensions and difficulty levels.

 License

This project is intended for educational and academic purposes.
