from llm import gemini_chat

class SynthesizerAgent:
    def __init__(self):
        self.role = "Synthesizer"
        self.prefix = (
            "You are a synthesizer agent. Combine all prior findings into a structured due diligence summary, highlighting the most important insights."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

synthesizer = SynthesizerAgent()