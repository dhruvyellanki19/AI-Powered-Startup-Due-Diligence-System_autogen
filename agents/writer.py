from llm import gemini_chat

class ReportWriterAgent:
    def __init__(self):
        self.role = "Report Writer"
        self.prefix = (
            "You are a report writer. Generate a professional, well-structured due diligence report with clear sections for market, product, tech, risks, and a final decision."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

report_writer = ReportWriterAgent()
