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
            return (False, ["Error: API key is not configured in .env"])

        prompt = f"""
Break the following complex task into a list of 3 to 5 simple, actionable subtasks.
Task: {task_description}

Respond only with the list of subtasks, one per line, each starting with a dash.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert task management assistant."},
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

            return (True, subtasks)

        except Exception as e:
            return (False, [f"Connection error: {e}"])