import os
from google import genai
from google.genai.types import HttpOptions
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            # Force "v1" to avoid "v1beta" errors
            self.client = genai.Client(
                api_key=self.api_key,
                http_options=HttpOptions(api_version="v1")
            )
        else:
            self.client = None

    def create_simple_tasks(self, task_description):
        if not self.client:
            return (False, ["Error: GEMINI_API_KEY is not configured."])

        prompt = f"""
Break the following complex task into a list of 3 to 5 simple, actionable subtasks.
Task: {task_description}

Respond only with the list of subtasks, one per line, each starting with a dash.
"""

        try:
            # Using gemini-2.5-flash, stable standard in 2026
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

            if not subtasks:
                return (False, ["Could not generate subtasks."])
            return (True, subtasks)

        except Exception as e:
            return (False, [f"Service error: {e}"])