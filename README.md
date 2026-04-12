# Task Manager IA

An intelligent command-line application for managing a task list (CRUD) with support for breaking down complex tasks using AI (Gemini or OpenAI).

## Features

- Basic CRUD operations: add, list, complete, and delete tasks.
- AI integration to break down complex tasks into simple subtasks.
- Data persistence in JSON format.
- Intuitive command-line interface.
- Support for multiple AI providers (Gemini and OpenAI).
- Unit tests included.

## Prerequisites

- Python 3.11 or higher (compatible with `list[Task]` type annotations).
- Virtual environment recommended for dependency isolation.
- API keys for AI services:
  - `GEMINI_API_KEY` for Google Gemini (optional, if using Gemini).
  - `OPENAI_API_KEY` for OpenAI (optional, if using OpenAI).
- Internet connection for AI features.

## Installation

1. Clone the repository:
   ```
   git clone <REPOSITORY_URL>
   cd taskManager_IA
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Linux/macOS:
   source .venv/bin/activate
   # On Windows:
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root (copy the existing one and replace the keys):
   ```
   GEMINI_API_KEY=your_gemini_key_here
   OPENAI_API_KEY=your_openai_key_here
   ```

2. In `main.py`, choose the AI service by commenting/uncommenting the corresponding lines:
   - For Gemini: `from src.services.ai.gemini_service import GeminiService as AIService`
   - For OpenAI: `from src.services.ai.openai_service import OpenAIService as AIService`

## Usage

Run the application:
```
python main.py
```

### Command Menu

- **1. Add task**: Enter a description to create a new task.
- **2. List tasks**: Display all pending and completed tasks.
- **3. Complete task**: Mark a task as completed by ID.
- **4. Delete task**: Delete a task by ID.
- **5. Complex task with AI**: Break down a complex task into subtasks using AI.
- **6. Exit**: Close the application.

### Examples

- Add task: Select 1 and type "Buy milk".
- Break down task: Select 5 and type "Organize a birthday party".

## Project Structure

- `main.py`: CLI entry point.
- `src/`
  - `core/`
    - `models.py`: `Task` data model.
    - `task_manager.py`: Task management logic (`TaskManager` with CRUD methods).
  - `database/`
    - `storage.py`: Data persistence (JSON).
  - `services/ai/`
    - `gemini_service.py`: Service for Google Gemini.
    - `openai_service.py`: Service for OpenAI.
- `tests/`
  - `test_task_manager.py`: Unit tests.
- `requirements.txt`: Project dependencies.
- `tasks.json`: Persistent data file.
- `.env`: Environment variables (do not include in version control).

## Testing

Run the unit tests:
```
python -m unittest tests/test_task_manager.py
```

## Contributing

1. Fork the repository.
2. Create a branch for your feature: `git checkout -b feature/new-feature`.
3. Make your changes and add tests.
4. Run tests: `python -m unittest tests/test_task_manager.py`.
5. Commit: `git commit -m "Add new feature"`.
6. Push: `git push origin feature/new-feature`.
7. Open a Pull Request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
   - `list`
   - `complete <id>` o `complet <id>`
   - `delete <id>`

## Mejora rápida sugerida (opcional)

- Documentar la forma en que `save_data`/`load_data` serializa (JSON, ruta, atomicidad).
- Añadir ejemplo de ejecución en README.
- Agregar `make test` o `poetry run` para workflow consistente.
- Opcional: mover tests a estructura de subcarpetas `tests/core/test_task_manager.py`.