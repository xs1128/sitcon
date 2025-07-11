from fastapi import FastAPI
from pydantic import BaseModel


# Inherit from Base Model
class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int


# list is an obj of list consisting of TodoItem(s)
todo_list : list[TodoItem] = []

app = FastAPI()


# If endpoint called call the func below
@app.get("/")
def root():
    return { "message" : "Hello, world!" }