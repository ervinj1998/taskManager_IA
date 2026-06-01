from src.core.task_manager import TaskManager
from src.services.ai.gemini_service import GeminiService as AIService # using alias for easy provider swap
#from src.services.ai.openai_service import OpenAIService as AIService


def print_menu():
    print("\n--- Intelligent Task Manager ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Complex task with AI")
    print("6. Exit")


def main():
    manager = TaskManager()
    ai_assistant = AIService()

    while True:
        print_menu()

        try:
            choice = int(input("Choose an option: "))

            match choice:
                case 1:
                    description = input("Enter a new task: ")
                    manager.add_task(description)

                case 2:
                    manager.list_task()

                case 3:
                    id = int(input("ID of the task to complete: "))
                    manager.complete_task(id)

                case 4:
                    id = int(input("ID of the task to delete: "))
                    manager.delete_task(id)

                case 5:
                    complex_task = input("Which task should the AI break down?: ")
                    print("Asking the AI...")

                    ok, subtasks = ai_assistant.create_simple_tasks(complex_task)

                    if ok:
                        for sub in subtasks:
                            manager.add_task(sub)
                        print(f"Successfully added {len(subtasks)} subtasks!")
                    else:
                        print(subtasks[0])

                case 6:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option. Please choose another.")

        except ValueError:
            print("Invalid option. Please choose another.")


if __name__ == "__main__":
    main()
