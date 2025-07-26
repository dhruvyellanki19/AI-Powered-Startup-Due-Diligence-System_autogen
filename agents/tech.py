from llm import gemini_chat

class TechAuditorAgent:
    def __init__(self):
        self.role = "Tech Auditor"
        self.prefix = (
            "You are a technology auditor. Evaluate the startup's tech stack, feasibility, architecture, scalability, security, and team capability."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

tech_auditor = TechAuditorAgent()
