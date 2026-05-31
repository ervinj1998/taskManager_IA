from src.core.models import Task
from src.database.storage import save_data, load_data


class TaskManager:
    def __init__(self):
        self._tasks: list[Task] = load_data()
        if self._tasks:
            self._next_id = self._tasks[-1].id + 1
        else:
            self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        save_data(self._tasks)
        print(f"Task added: {description}")

    def list_task(self):
        if not self._tasks:
            print("No pending tasks.")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                save_data(self._tasks)
                print(f"Task completed: {task.description}")
                return
        print(f"Task not found: #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                save_data(self._tasks)
                print(f"Task deleted: #{task.id}")
                return
        print(f"Task not found: #{id}")
