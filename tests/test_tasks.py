import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import crud

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_state():
    crud.reset_state()
    yield

def test_create_and_get_task():
    # crear
    resp = client.post("/tasks", json={"title": "Examen Cálculo"})
    assert resp.status_code == 201
    task = resp.json()
    assert task["id"] == 1
    assert task["status"] == "pending"

    # obtener
    resp = client.get("/tasks/1")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Examen Cálculo"

def test_list_tasks():
    client.post("/tasks", json={"title": "Proyecto Mecatrónica"})
    client.post("/tasks", json={"title": "Leer capítulo IA"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.json()) == 2

def test_update_task():
    client.post("/tasks", json={"title": "Ensayo Ética"})
    resp = client.put("/tasks/1", json={"status": "in_progress"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "in_progress"

def test_delete_task():
    client.post("/tasks", json={"title": "Exposición Física"})
    resp = client.delete("/tasks/1")
    assert resp.status_code == 204
    resp = client.get("/tasks/1")
    assert resp.status_code == 404

def test_reject_empty_title():
    resp = client.post("/tasks", json={"title": "   "})
    assert resp.status_code == 422  # valida Pydantic

def test_reject_invalid_status():
    resp = client.post("/tasks", json={"title": "TP", "status": "weird"})
    assert resp.status_code == 422

def test_get_task_not_found():
    resp = client.get("/tasks/999")  # no existe
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Task not found"


def test_update_task_not_found():
    resp = client.put("/tasks/999", json={"status": "done"})
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Task not found"


def test_delete_task_not_found():
    resp = client.delete("/tasks/999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Task not found"
