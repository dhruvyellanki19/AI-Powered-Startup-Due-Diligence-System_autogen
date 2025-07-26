import os
from dotenv import load_dotenv
from autogen.agentchat.llm_clients import GeminiChatClient

load_dotenv()
llm = GeminiChatClient(model="models/gemini-pro") 