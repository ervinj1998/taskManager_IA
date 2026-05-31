class Task:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        # Checkmark for completed, space for pending
        status = "✔" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
