from llm import gemini_chat

class ProductReviewerAgent:
    def __init__(self):
        self.role = "Product Reviewer"
        self.prefix = (
            "You are a product reviewer. Critically evaluate the startup's product for differentiation, user need, usability, scalability, and go-to-market readiness."
        )

    def run(self, question, startup_description):
        prompt = f"{self.prefix}\n\nStartup Description:\n{startup_description}\n\nQuestion:\n{question}"
        return gemini_chat(prompt)

product_reviewer = ProductReviewerAgent()
