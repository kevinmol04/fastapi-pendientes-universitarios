from typing import Dict, List
from .models import Task, TaskCreate, TaskUpdate, TaskStatus

# --- Estado en memoria ---
_TASKS: Dict[int, Task] = {}
_NEXT_ID: int = 1


def _next_id() -> int:
    global _NEXT_ID
    nid = _NEXT_ID
    _NEXT_ID += 1
    return nid


def reset_state() -> None:
    """Para pruebas: limpia el store y reinicia el ID."""
    global _TASKS, _NEXT_ID
    _TASKS = {}
    _NEXT_ID = 1


# --- Operaciones CRUD ---
def list_tasks() -> List[Task]:
    return list(_TASKS.values())


def create_task(payload: TaskCreate) -> Task:
    tid = _next_id()
    task = Task(id=tid, **payload.model_dump())
    _TASKS[tid] = task
    return task


def get_task(task_id: int) -> Task | None:
    return _TASKS.get(task_id)


def update_task(task_id: int, payload: TaskUpdate) -> Task | None:
    existing = _TASKS.get(task_id)
    if not existing:
        return None
    data = existing.model_dump()
    updates = payload.model_dump(exclude_unset=True)
    data.update(updates)
    updated = Task(**data)
    _TASKS[task_id] = updated
    return updated


def delete_task(task_id: int) -> bool:
    return _TASKS.pop(task_id, None) is not None
