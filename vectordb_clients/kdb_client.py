import kdbai_client as kdbai
from vectordb_clients.basedb_client import VectorDBClient
from configs.config import Config

class KDBAIClient(VectorDBClient):
    def __init__(self):
        self.session    = kdbai.Session(api_key=Config.KDBAI_API_KEY, endpoint=Config.KDBAI_ENDPOINT)
        self.db         = self.session.database('default')

        self.table_schema = [
            {"name": "chunk_data", "type": "str"},
            {"name": "media_type", "type": "str"},
            {
                "name": "embeddings",
                "type": "float32s",
            },
        ]

        self.indexes = [
            {
                'type': 'qFlat',
                'name': 'qflat_index',
                'column': 'embeddings',
                'params': {'dims': 1024, 'metric': "CS"},
            },
        ]

        try:
            self.db.table("rag_store").drop()
        except kdbai.KDBAIException:
            pass

        self.table = self.db.create_table(table="rag_store", schema=self.table_schema, indexes=self.indexes)

    def store_embedding(self, embedded_df, opts={}):
        from tqdm import tqdm
        chunk_size = opts.get("chunk_size")

        for i in tqdm(range(0, embedded_df.shape[0], chunk_size)):
            self.table.insert(embedded_df[i:i+chunk_size].reset_index(drop=True))

    def retrieve_similar(self, query_embedding):
        return self.table.search(vectors={"qflat_index":[query_embedding]}, n=2)
