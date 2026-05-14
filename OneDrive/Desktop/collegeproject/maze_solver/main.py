from fastapi import FastAPI
from backend.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Maze Solver API",
    description="Backend for maze solving algorithms",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)