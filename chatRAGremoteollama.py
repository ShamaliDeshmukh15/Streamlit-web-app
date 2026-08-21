import streamlit as st
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="C++ RAG Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 C++ RAG Chatbot using Ollama")

# -----------------------------
# Load & Process Data
# -----------------------------
@st.cache_resource
def load_vectorstore():

    # Load C++ text file
    loader = TextLoader(
        "C++_Introduction.txt",
        encoding="utf-8"
    )

    documents = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    final_docs = text_splitter.split_documents(documents)

    # -----------------------------
    # Hugging Face Embedding Model
    # -----------------------------
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vector database
    db = FAISS.from_documents(
        final_docs,
        embeddings
    )

    return db


# Load vector database
db = load_vectorstore()


# -----------------------------
# Load LLM using Ollama
# -----------------------------
llm = Ollama(
    model="gemma2:2b"
)


# -----------------------------
# Chat Interface
# -----------------------------
user_question = st.text_input(
    "Ask a question about C++:"
)

if user_question:

    with st.spinner("Thinking..."):

        # Search for relevant documents
        docs = db.similarity_search(
            user_question,
            k=4
        )

        # Combine retrieved text
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # -----------------------------
        # RAG Prompt
        # -----------------------------
        prompt = f"""
You are a helpful C++ programming assistant.

Answer the question using ONLY the context provided below.

If the answer is not available in the context,
say:

"I don't know based on the provided document."

Context:
--------------------
{context}
--------------------

Question:
{user_question}

Answer:
"""

        # Generate answer using Ollama
        response = llm.invoke(prompt)

        # Display answer
        st.subheader("Answer:")
        st.write(response)
