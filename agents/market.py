from llm import gemini_chat

class MarketAnalystAgent:
    def __init__(self):
        self.role = "Market Analyst"
        self.prefix = (
            "You are a market analyst. Analyze the startup's industry, market size, trends, and potential for growth. Be specific, concise, and reference current market conditions."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

market_analyst = MarketAnalystAgent()
