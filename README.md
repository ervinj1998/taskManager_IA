# Task Manager IA

An intelligent command-line application for managing a task list (CRUD) with **optional** support for breaking down complex tasks using AI (Google Gemini or OpenAI).

> 💡 **The app works fully without an API key.** Only the AI-powered "complex task breakdown" feature (option 5) requires one.

---

## 🚀 Quickstart

```bash
git clone https://github.com/ervinj1998/taskManager_IA.git
cd taskManager_IA
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                # Optional: only needed for the AI feature
python main.py
```

That's it — the app will start and you can use options 1–4 right away.

---

## ✨ Features

- Basic CRUD operations: add, list, complete, and delete tasks.
- Data persistence in JSON format.
- Interactive command-line menu.
- **Optional** AI integration to break down complex tasks into subtasks.
- Support for two AI providers: Google Gemini and OpenAI.
- Unit tests included.

---

## 📋 Prerequisites

- **Python 3.11 or higher** (required for `list[Task]` type annotations).
- Virtual environment recommended.
- Internet connection — only if you use the AI feature.

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ervinj1998/taskManager_IA.git
   cd taskManager_IA
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3.11 -m venv .venv
   ```
   - **Linux / macOS:** `source .venv/bin/activate`
   - **Windows:** `.venv\Scripts\activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python main.py
   ```

✅ At this point options 1–4 (add, list, complete, delete) work without any extra setup.

---

## 🔑 AI Configuration (Optional)

If you want to try the **"Complex task with AI"** feature (option 5), follow these steps. Otherwise, you can skip this section.

### 1. Get a free API key

- **Google Gemini** (recommended — has a free tier):  
  👉 https://aistudio.google.com/app/apikey

- **OpenAI** (paid, requires billing setup):  
  👉 https://platform.openai.com/api-keys

### 2. Create your `.env` file

```bash
cp .env.example .env
```

Then open `.env` and paste your key (only fill the one you'll use):

```env
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
```

### 3. Choose the provider in `main.py`

Comment/uncomment the import line for the provider you want:

```python
from src.services.ai.gemini_service import GeminiService as AIService
# from src.services.ai.openai_service import OpenAIService as AIService
```

---

## 🖥️ Usage

Run:
```bash
python main.py
```

You'll see an interactive menu:

| Option | Action |
|--------|--------|
| 1 | Add task |
| 2 | List tasks |
| 3 | Complete task (by ID) |
| 4 | Delete task (by ID) |
| 5 | Break down complex task with AI *(requires API key)* |
| 6 | Exit |

### Examples

- **Add a task:** select `1` and type `Buy milk`.
- **Break down a task with AI:** select `5` and type `Organize a birthday party`.

---

## 📁 Project Structure

```
taskManager_IA/
├── main.py                  # CLI entry point
├── src/
│   ├── core/
│   │   ├── models.py        # Task data model
│   │   └── task_manager.py  # CRUD logic (TaskManager)
│   ├── database/
│   │   └── storage.py       # JSON persistence
│   └── services/ai/
│       ├── gemini_service.py
│       └── openai_service.py
├── tests/
│   └── test_task_manager.py # Unit tests
├── requirements.txt
├── .env.example             # Template for environment variables
├── tasks.json               # Auto-generated: persistent task storage
└── README.md
```

---

## 🧪 Testing

Run the unit tests:
```bash
python -m unittest discover tests
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`.
3. Make your changes and add tests.
4. Run the tests: `python -m unittest discover tests`.
5. Commit: `git commit -m "Add new feature"`.
6. Push: `git push origin feature/new-feature`.
7. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.