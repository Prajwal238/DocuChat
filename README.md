# 📄 DocuChat

**DocuChat** is a Retrieval-Augmented Generation (RAG) application designed to provide intelligent, context-aware answers from your document collections. By combining the power of large language models with efficient document retrieval, DocuChat enables users to interact with their data in a conversational manner.

---

## 🚀 Features

- **Conversational Q&A**: Ask questions and get accurate, context-rich answers from your documents.
- **Document Upload & Indexing**: Easily add new documents to your knowledge base.
- **Semantic Search**: Retrieve relevant passages using advanced embedding models.
- **Scalable Codebase**: Built with scalability in mind for future enhancements.
- **User-Friendly Interface**: Clean, intuitive UI for seamless interactions.

---

## 🛠️ Tech Stack

- **Backend**: Python  
- **Frontend**: Streamlit  
- **Vector Store**: KDB  
- **Embedding Model**: Voyage AI  
- **Indexing Strategy**: Basic chunking of documents  
- **LLM**: Gemini AI  

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/docuchat.git
   cd docuchat


2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set up environment variables:**
   - Create a .env file in the project root.
   - Add your API keys and configuration (e.g., Gemini AI API key, KDB connection details).


4. **Run the application:**
   ```bash
   streamlit run app/main.py

---

## 📝 Usage

Open your browser and navigate to the Streamlit URL provided in your terminal (usually http://localhost:8501).
Upload documents or connect to your data source.
Start chatting! Ask questions and receive answers grounded in your documents.

## 📚 Example
**User:** *What is the refund policy in our latest terms document?*
**DocuChat:** *According to "Terms_2024.pdf", the refund policy states...*

## ⚙️ Configuration

Vector Store: Configure KDB connection in your config files.
LLM Provider: Set your Gemini AI API keys and model preferences in .env.
Document Sources: Add or modify document ingestion scripts as needed.

## 🔭 Future Scope

Plugin Support: DocuChat aims to support a plugin system in future releases, allowing users to easily plug in different embedding models or indexing strategies from a list of available options—making the backend more customizable without code changes.

## 🧑‍💻 Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.
