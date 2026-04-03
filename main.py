from src.core.task_manager import TaskManager

def print_menu():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    # Instanciamos el gestor de tareas
    manager = TaskManager()

    while True:
        
        print_menu()

        choice = input("Elige una opción: ")

        match choice:
            case "1":
                description = input("Crea nueva tarea: ")
                manager.add_task(description)
                
            case "2":
                manager.list_task()# Aquí llamaremos a manager.list_tasks()
                
            case "3":
                id = input("ID de la tarea a completar: ")
                manager.complet_task(id)# Aquí pediremos el ID y llamaremos a manager.complete_task()
                
            case "4":
                id = input("ID de la tarea a eliminar: ")# Aquí pediremos el ID y llamaremos a manager.delete_task()
                manager.complet_task(id)
                
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Selecciona otra.")

if __name__ == "__main__":
    main()