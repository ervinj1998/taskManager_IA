# Task Manager IA

Una aplicación de línea de comandos para gestionar una lista de tareas (CRUD).

Incluye:

- Modelo de datos `Task` en `src/core/models.py`
- Lógica de gestión en `src/core/task_manager.py`
- Persistencia de datos en `src/database/storage.py`
- CLI en `main.py`
- Pruebas unitarias en `tests/test_task_manager.py`

## Estructura del repositorio

- `main.py`: punto de entrada CLI
- `src/`
  - `core/`
    - `models.py`: clase `Task`
    - `task_manager.py`: clase `TaskManager` con `add_task`, `list_task`, `complet_task`, `delete_task`
  - `database/`
    - `storage.py`: manejo de `save_data`/`load_data` (JSON u otro backend)
- `tests/`
  - `test_task_manager.py`: pruebas unitarias para funciones principales
- `README.md`: documentación
- `LICENSE`: licencia

## Requisitos previos

- Python 3.11+ (compatible con anotaciones `list[Task]`)
- Entorno virtual recomendado:
  - `python -m venv .venv`
  - Linux/macOS: `source .venv/bin/activate`
  - Windows: `.venv\Scripts\activate`
- Dependencias: solo `unittest` integrado, no requiere instalación adicional

## Instalación y uso

1. Clonar:
   - `git clone <repo>`
   - `cd taskManager_IA`

2. Activar entorno:
   - `source .venv/bin/activate` (o equivalente)

3. Ejecutar:
   - `python main.py`
   - O desde `src` si CLI ofrece comandos: `python -m src.cli ...` (revisar implementación)

4. Comandos típicos (según implementado):
   - `add <descripción>`
   - `list`
   - `complete <id>` o `complet <id>`
   - `delete <id>`

## Mejora rápida sugerida (opcional)

- Documentar la forma en que `save_data`/`load_data` serializa (JSON, ruta, atomicidad).
- Añadir ejemplo de ejecución en README.
- Agregar `make test` o `poetry run` para workflow consistente.
- Opcional: mover tests a estructura de subcarpetas `tests/core/test_task_manager.py`.