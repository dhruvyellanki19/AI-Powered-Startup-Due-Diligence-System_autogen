from llm import gemini_chat

class VCPartnerAgent:
    def __init__(self):
        self.role = "VC Partner"
        self.prefix = (
            "You are a venture capital (VC) partner. Review the final due diligence report and give a GO or NO-GO investment decision with strong justification."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

vc_partner = VCPartnerAgent()
