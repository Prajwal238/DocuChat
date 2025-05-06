from abc import ABC, abstractmethod

class EmbeddingModel(ABC):
    """Abstract class for AI embedding service."""
    @abstractmethod
    def get_embedding(self, text: str):
        pass