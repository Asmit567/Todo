from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

tododb = []

# Model created for todo
class Post(BaseModel):
    id: int
    status: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False

 

@app.get("/todo")
def get_todo():
    return tododb


@app.post("/todo")
def add_todo(todo: Post):
    tododb.append(todo.dict())
    return tododb[-1]


@app.get("/todo/{id}")
def get_todo(id: int):
    todo = id - 1
    return tododb[todo]

@app.post("/todo/{id}")
def update_todo(id: int, todo: Post):
    tododb[id] = todo
    return {"message": "todo has been updated succesfully"}

@app.delete("/todo/{id}")
def delete_todo(id: int):
    tododb.pop(id-1)
    return {"message": "todo has been deleted succesfully"}
