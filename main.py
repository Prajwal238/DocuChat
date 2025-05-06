# from embedding_models.voyage_embedding import VoyageAIEmbeddingModel
# from vectordb_clients.kdb_client import KDBAIClient
# from services.rag_service import RAGService
# from llm_models.gemini import GeminiModel
# import streamlit as st
# import io
# import os

# def main():

#     embedding_model     = VoyageAIEmbeddingModel()
#     vector_db_client    = KDBAIClient()
#     llm_model           = GeminiModel()

#     rag_service = RAGService(embedding_model, vector_db_client, llm_model)

#     st.title("Talk to your PDF")
#     uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

#     if(uploaded_file):
#         file_path = os.path.join('data/text/', uploaded_file.name)
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#         st.success(f"PDF saved at: {file_path}")

#     query = st.text_input("Ask your Query: ")
#     if st.button("Ask"):
#         with st.spinner("Retrieving answer..."):

#             ai_response = rag_service.process_query(query)
#             st.write("### Response: ")
#             st.write(ai_response.text)
    

# if __name__ == "__main__":
#     main()

import os
import streamlit as st
import base64
import uuid
from embedding_models.voyage_embedding import VoyageAIEmbeddingModel
from vectordb_clients.kdb_client import KDBAIClient
from services.rag_service import RAGService
from llm_models.gemini import GeminiModel
from db.DBManager import DBManager
# Define storage directory
UPLOAD_DIR = "data/text/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

if "userContext" not in st.session_state:
    st.session_state.userContext = {
        "userId": base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')
    }

st.title("Talk to Your PDF")

# File upload
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    uploaded_file.name = st.session_state.userContext["userId"] + uploaded_file.name
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.file_path = file_path  # Store file path in session state
    st.success(f"PDF saved at: {file_path}")

# **Initialize RAGService after file upload**
if "file_path" in st.session_state and "rag_service" not in st.session_state:
    with st.spinner("Initializing RAG Service..."):
        # Initialize DBManager
        db_manager = DBManager()
        st.session_state.db = db_manager.connect()
        st.session_state.embedding_model = VoyageAIEmbeddingModel()
        st.session_state.vector_db_client = KDBAIClient()
        st.session_state.llm_model = GeminiModel()
        
        st.session_state.rag_service = RAGService(
            st.session_state.embedding_model,
            st.session_state.vector_db_client,
            st.session_state.llm_model,
            st.session_state.db,
            st.session_state.userContext
        )
    
    st.success("RAG Service initialized and embeddings created!")

# Query input
query = st.text_input("Ask your Query:")

if st.button("Ask"):
    if "rag_service" not in st.session_state:
        st.error("Please upload a PDF first!")
    else:
        with st.spinner("Retrieving answer..."):
            ai_response = st.session_state.rag_service.process_query(query)
            st.write("### Response:")
            st.write(ai_response.text)
