from llm import gemini_chat

class InvestmentAdvisorAgent:
    def __init__(self):
        self.role = "Investment Advisor"
        self.prefix = (
            "You are an investment advisor. Decide the startup’s investability based on team, traction, market, product, tech, and risks. Justify your recommendation."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

investment_advisor = InvestmentAdvisorAgent()
