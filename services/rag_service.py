from extractors.document_extractor import DocumentLoader
from extractors.image_extractor import ImageLoader
from utils.util import Utils
import pandas as pd
from datetime import datetime

class RAGService:
    def __init__(self, embedding_model, vector_db_client, llm_model, db, userContext):
        
        self.embedding_model    = embedding_model
        self.vector_db_client   = vector_db_client
        self.llm_model          = llm_model
        self.db                 = db
        self.userContext        = userContext
        self._load_data()

    def _load_data(self):
        doc_loader_inst = DocumentLoader(filePath='./data/text')
        img_loader_inst = ImageLoader(filePath='./data/images')

        df = pd.DataFrame(columns=['chunk_data', 'media_type', 'embeddings'])
        opts = {
            "df": df,
            "pd": pd
        }

        img_data = img_loader_inst.load_images(path='/home/Prajwal.Katakam/Downloads/rag_resources/rag_project/data/images/', opts=opts)
        doc_data = doc_loader_inst.load_documents(path= '/home/Prajwal.Katakam/Downloads/rag_resources/rag_project/data/text/', opts=opts)

        df  = opts["df"]

        data = img_data + doc_data

        embeddings          = self.embedding_model.get_embedding(data=data)
        df["embeddings"]    = embeddings

        self.vector_db_client.store_embedding(embedded_df=df, opts={"chunk_size": 2000})


    def process_query(self, query: str):
        """Processes a user query, retrieves similar documents."""
        
        #query
        user_query = query
        query = query if type(query) is list else [query]
        
        #embedding
        embedding = self.embedding_model.get_embedding(query, {"isQuery": True})
        embedding = embedding[0]
        
        #retreiving
        results             = self.vector_db_client.retrieve_similar(embedding)
        retrieved_rag_data  = Utils().retrieved_rag_data(results=results)

        #get conversation history
        from dbModels.conversationHistoryModel import ConversationHistoryModel
        conversationHistoryModel = ConversationHistoryModel(self.db)
        conversation_history = conversationHistoryModel.get_conversation_history_by_user_id(self.userContext["userId"])
        if(len(conversation_history) > 0):
            conversation_history = conversation_history[0]
            conversation_history = "\n".join([f"User: {item['user_query']}\nAI: {item['response']}" for item in conversation_history['conversation']])
        else:
            conversation_history = ""
        
        #prompt preparation
        template    = """Answer the question based only on the following context and conversation history:
                    {context}

                    {conversation_history}

                    Question: {question}
                    """
        prompt      = template.format(context="\n".join(retrieved_rag_data), conversation_history=conversation_history, question= user_query)

        #generating
        response = self.llm_model.generate_response(prompt=prompt)

        #save conversation history
        if(len(conversation_history) == 0):
            conversation_history = {
                "_id":  self.userContext["userId"],
                "conversation": [{
                    "user_query": user_query,
                    "response": response.text
                }],
                "timestamp": datetime.now().isoformat()
            }
            conversationHistoryModel.insert_conversation_history(conversation_history)
        else:
            new_conversation = {
                "user_query": user_query,
                "response": response.text
            }
            conversationHistoryModel.update_conversation_history({"_id": self.userContext["userId"]}, new_conversation)
        return response