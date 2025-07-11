from fastapi import FastAPI
from router import todo

app = FastAPI()

app.include_router(
    todo.router,
    prefix = "/prefix",
    tags = ["todos"]
)