from fastapi import APIRouter
from backend.models import MazeInput, MazeOutput
from backend.solver_service import solve_maze

router = APIRouter()


@router.post("/solve-maze", response_model=MazeOutput)

def solve_maze_api(data: MazeInput):

    path = solve_maze(
        data.maze,
        data.start,
        data.goal,
        data.algorithm
    )

    return {"path": path}