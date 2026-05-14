from pydantic import BaseModel
from typing import List

class MazeInput(BaseModel):

    maze: List[List[int]]
    start: List[int]
    goal: List[int]
    algorithm: str


class MazeOutput(BaseModel):

    path: List[List[int]]