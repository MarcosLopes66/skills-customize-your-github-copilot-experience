from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    completed: Optional[bool] = None


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


# Temporary in-memory storage; data is cleared when the server restarts.
tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: Create a task, store it, and return it.
    pass


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    # TODO: Update the provided fields or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status 404.
    pass
