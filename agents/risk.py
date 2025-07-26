from llm import gemini_chat

class RiskOfficerAgent:
    def __init__(self):
        self.role = "Risk Officer"
        self.prefix = (
            "You are a risk officer. Identify any business, legal, regulatory, technical, or team-related risks that could impact the startup."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

risk_officer = RiskOfficerAgent()
