import json
import os
from src.core.models import Task

FILENAME = "tasks.json"

def save_data(tasks):
    """Convierte la lista de objetos Task en JSON y la guarda."""
    data = [
        {"id": t.id, "description": t.description, "completed": t.completed} 
        for t in tasks]
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    """Lee el JSON y devuelve una lista de objetos Task."""
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            return [Task(item["id"], item["description"], item["completed"]) for item in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []