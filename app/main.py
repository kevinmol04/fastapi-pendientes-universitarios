from fastapi import FastAPI, HTTPException, status
from typing import List

from .models import Task, TaskCreate, TaskUpdate
from . import crud

app = FastAPI(title="API Pendientes Universitarios")

# Constante para evitar duplicación de string
NOT_FOUND_MSG = "Task not found"


def _raise_not_found():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MSG)


@app.get("/", tags=["health"])
def read_root():
    return {"message": "API Pendientes Universitarios corriendo 🚀"}


# --- Endpoints Tasks ---
@app.get("/tasks", response_model=List[Task], tags=["tasks"])
def list_tasks():
    return crud.list_tasks()


@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["tasks"],
)
def create_task(payload: TaskCreate):
    return crud.create_task(payload)


@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int):
    task = crud.get_task(task_id)
    if not task:
        _raise_not_found()
    return task


@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, payload: TaskUpdate):
    task = crud.update_task(task_id, payload)
    if not task:
        _raise_not_found()
    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["tasks"],
)
def delete_task(task_id: int):
    ok = crud.delete_task(task_id)
    if not ok:
        _raise_not_found()
    return None
