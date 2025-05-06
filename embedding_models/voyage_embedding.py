from embedding_models.base_embedding import EmbeddingModel
from voyageai import Client
from configs.config import Config

class VoyageAIEmbeddingModel(EmbeddingModel):

    def __init__(self):
        self.client = Client(api_key=Config.VOYAGEAI_API_KEY)

    def get_embedding(self, data, opts={}):
        """Generates an embedding for a given data or the given input query."""
        if(opts.get("isQuery")):
            input_type = None
            data       = [data]
        else:
            input_type = "document"
        vc = self.client
        result = vc.multimodal_embed(inputs=data, model=Config.MODEL_NAME, input_type=input_type)
        return result.embeddings