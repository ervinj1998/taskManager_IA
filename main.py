from src.core.task_manager import TaskManager
from src.services.ai.gemini_service import GeminiService as AIService #usando alias para cambiar de proveedor cualquier momento
#from src.services.ai.openai_service import OpenAIService as AIService

def print_menu():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Tarea compleja con IA")
    print("6. Salir")

def main():
    # Instanciamos el gestor de tareas
    manager = TaskManager()
    ai_assistant = AIService()

    while True:
        
        print_menu()

        try:
            choice = int(input("Elige una opción: "))

            match choice:
                case 1:
                    description = input("Crea nueva tarea: ")
                    manager.add_task(description)
                    
                case 2:
                    manager.list_task()
                    
                case 3:
                    id = int(input("ID de la tarea a completar: "))
                    manager.complet_task(id)
                    
                case 4:
                    id = int(input("ID de la tarea a eliminar: "))
                    manager.delete_task(id)
                
                case 5:
                    complex_task = input("¿Qué tarea quieres que la IA desglose?: ")
                    print("Consultando al cerebro artificial...")
                    
                    subtareas = ai_assistant.create_simple_tasks(complex_task)
                    
                    # Verificamos si no es un mensaje de error
                    if subtareas and "Error" not in subtareas[0]:
                        for sub in subtareas:
                            manager.add_task(sub) # Las añadimos al manager una por una
                        print(f"¡Se han añadido {len(subtareas)} subtareas con éxito!")
                    else:
                        print(subtareas[0])

                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida. Selecciona otra.")
            
        except ValueError:
            print("Opción no válida. Selecciona otra.")

if __name__ == "__main__":
    main()