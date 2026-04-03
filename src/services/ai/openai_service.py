import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def create_simple_tasks(self, task_description):
        if not self.api_key:
            return ["Error: La API KEY no está configurada en el .env"]

        prompt = f"""
        Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
        Tarea: {task_description}
        
        Responde solo con la lista de subtareas, una por línea, empezando con un guion.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un asistente experto en gestión de tareas."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )

            content = response.choices[0].message.content.strip()
            
            subtasks = []
            for line in content.split("\n"):
                line = line.strip()
                if line and line.startswith("-"):
                    subtasks.append(line[1:].strip())
            
            return subtasks

        except Exception as e:
            return [f"Error de conexión: {str(e)}"]