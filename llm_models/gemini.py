import google.generativeai as genai
from .base_llm import LLMModel
from configs.config import Config

class GeminiModel(LLMModel):
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL_NAME)

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response
