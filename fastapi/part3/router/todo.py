from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int = Field(gt = 0)


todo_list : list[TodoItem] = []


@router.get("/")
def root():
    return { "message" : "Hello world" }


@router.get("/todos")
def get_todos() -> list[TodoItem]:
    return todo_list


@router.post("/todos")
def add_todo(todo: TodoItem) -> TodoItem:
    todo_list.append(todo)
    return todo


@router.put("/todo/{id}")
def update_todo(id: int, todo: TodoItem) -> TodoItem:
    if len(todo_list) - 1 <= id: # 改寫 if 判斷，當找不到的時候就丟出錯誤
        raise HTTPException(status_code=404, detail="Item not found") # 這邊回傳錯誤，而不是待辦事項
    todo_list[id] = todo
    return todo


@router.delete("/todo/{id}")
def delete_todo(id: int):
    if len(todo_list) - 1 <= id: # 改寫 if 判斷，當找不到的時候就丟出錯誤
        raise HTTPException(status_code=404, detail="Item not found") # 這邊回傳錯誤，而不是待辦事項
    todo_list.pop(id)
    return


@router.get("/todo/{id}")
def get_todo(id: int) -> TodoItem:
    if len(todo_list) - 1 <= id: # 改寫 if 判斷，當找不到的時候就丟出錯誤
        raise HTTPException(status_code=404, detail="Item not found") # 這邊回傳錯誤，而不是待辦事項
    return todo_list[id]