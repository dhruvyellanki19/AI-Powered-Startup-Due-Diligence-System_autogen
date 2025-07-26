from llm import gemini_chat

class CompetitorScoutAgent:
    def __init__(self):
        self.role = "Competitor Scout"
        self.prefix = (
            "You are a competitor scout. List the major competitors, compare features, pricing, traction, and identify competitive advantages or threats."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

competitor_scout = CompetitorScoutAgent()
