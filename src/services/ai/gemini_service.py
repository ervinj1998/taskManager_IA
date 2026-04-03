import os
from google import genai
from google.genai.types import HttpOptions
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            # Forzamos la versión "v1" para evitar el error de "v1beta"
            self.client = genai.Client(
                api_key=self.api_key,
                http_options=HttpOptions(api_version="v1")
            )
        else:
            self.client = None

    def create_simple_tasks(self, task_description):
        if not self.client:
            return ["Error: GEMINI_API_KEY no configurada."]

        prompt = f"""
        Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
        Tarea: {task_description}
        
        Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guion.
        """

        try:
            # Usamos gemini-2.5-flash, que es el estándar estable en 2026
            response = self.client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt
            )
            
            content = response.text.strip()
            
            subtasks = []
            for line in content.split("\n"):
                line = line.strip()
                if line and line.startswith("-"):
                    subtasks.append(line[1:].strip())
            
            return subtasks if subtasks else ["No se pudieron generar subtareas."]
            
        except Exception as e:
            # Si el error persiste, esto nos dirá exactamente por qué
            return [f"Error técnico en el servicio: {str(e)}"]