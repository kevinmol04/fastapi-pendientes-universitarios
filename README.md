# FastAPI - Pendientes Universitarios

Este proyecto implementa un **microservicio de gestión de tareas (ToDo)** para estudiantes universitarios, construido con **FastAPI**.  
Permite **crear, listar, actualizar y eliminar tareas** de manera sencilla, con validaciones básicas y pruebas automatizadas.

---

## Tecnologías utilizadas
- **Python 3.11**
- **FastAPI** para la API REST.
- **Pytest** para pruebas unitarias e integración.
- **SonarQube** para análisis de calidad de código y cobertura.
- **GitHub Actions** para CI/CD.
- **Postman** para pruebas manuales de endpoints.

---

## Endpoints principales
- `GET /tasks` → Lista todas las tareas.
- `POST /tasks` → Crea una nueva tarea.
- `GET /tasks/{id}` → Obtiene una tarea por ID.
- `PUT /tasks/{id}` → Actualiza una tarea existente.
- `DELETE /tasks/{id}` → Elimina una tarea.

Modelo de Tarea:
```json
{
  "id": 1,
  "title": "Examen Cálculo",
  "description": "Estudiar capítulo 5",
  "status": "pending"
}

