from abc import ABC, abstractmethod

class LLMModel(ABC):
    """Abstract class for AI embedding service."""
    @abstractmethod
    def generate_response(self, text: str):
        pass