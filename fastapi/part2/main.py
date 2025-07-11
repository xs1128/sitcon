from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# import sys


class TodoItem(BaseModel):
    """
    Consist of 4 different properties for a Todo List Item
    """
    title: str
    description: str
    completed: bool
    priority: int


# List of TodoItem instances to be stored temporarily
todo_list : list[TodoItem] = []

# Initialize the API
app = FastAPI()


# Just to return a message
@app.get("/")
def root():
    return { "message" : "Hello world" }


# Return all todos in currrent list
@app.get("/todos")
def get_todos() -> list[TodoItem]:
    return todo_list


# Add a TodoItem to the end of the list
@app.post("/todos")
def add_todo(todo: TodoItem) -> TodoItem:
    todo_list.append(todo)
    return todo


# Update certain id's TodoItem
@app.put("/todo/{id}")
def update_todo(id: int, todo: TodoItem) -> TodoItem:
    # Error handling for Index Error
    if len(todo_list) - 1 <= id:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Alternate form
    # try:
    todo_list[id] = todo
    return todo
    # except IndexError:
    #     sys.stderr("Hehe")


# Remove todo_list[id] from list
@app.delete("/todo/{id}")
def delete_todo(id: int):
    if len(todo_list) - 1 <= id:
        raise HTTPException(status_code=404, detail="Item not found")
    todo_list.pop(id)


# Access todo_list[id]: the value at the id's index 
# of todo_list start counting from 0
@app.get("/todo/{id}")
def get_todos(id: int) -> TodoItem:
    if len(todo_list) - 1 <= id:
        raise HTTPException(status_code=404, detail="Item not found")
    return todo_list[id]

# 試著寫出拿特定 id 待辦事項 Endpoint ;(