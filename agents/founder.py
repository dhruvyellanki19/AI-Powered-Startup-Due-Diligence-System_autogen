from llm import gemini_chat

class FounderAgent:
    def __init__(self):
        self.role = "Startup Founder"
        self.prefix = (
            "You are the startup founder. Provide detailed and honest responses to any questions about your startup, vision, team, product, and challenges."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

founder = FounderAgent()
