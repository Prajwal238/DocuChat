import os
import io
from utils.util import Utils

class DocumentLoader():
    
    def __init__(self, filePath):
        self.texts = os.listdir(filePath)

    def load_documents(self, path, opts={}):
        texts       = self.texts
        text_data   = []
        # df          = opts.get("df")
        pd          = opts.get("pd")

        for text in texts:
            
            text_path = path + text
            # Do the indexing(RAG) here

            extracted_doc = Utils().read_text_from_file(filename=text_path)
            chunks = self.chunk_document(extracted_doc=extracted_doc)
            
            for chunk in chunks:
                text_data.append([chunk])
                new_row     = {
                    'chunk_data': chunk,
                    'media_type': "text",
                    'embeddings': ""
                }
                opts["df"]  = pd.concat([opts["df"], pd.DataFrame([new_row])], ignore_index=True)
        
        return text_data

    def chunk_document(self, extracted_doc):
        # chunks = [chunk.strip() for chunk in extracted_doc.split("\n\n") if chunk.strip()]
        chunks = [chunk.strip() for chunk in extracted_doc.split("##") if chunk.strip()]
        return chunks