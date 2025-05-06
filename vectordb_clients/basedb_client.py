from abc import ABC, abstractmethod

class VectorDBClient(ABC):
    """Abstract class for VectorDB storage & retrieval."""
    @abstractmethod
    def store_embedding(self, text: str, embedding: list):
        pass

    @abstractmethod
    def retrieve_similar(self, embedding: list):
        pass
