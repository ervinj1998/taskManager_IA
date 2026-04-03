from src.core.models import Task

class TaskManager: 
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")

    def list_task(self):
        if not self._tasks:
            print("No pending tasks.")
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        for task in self._tasks:
            if task.id==id:
                task.completed = True
                print(f"Tarea completada: {id}")
                return
        print(f"Tarea no encontrada: #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id==id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")