import os
import tempfile
import shutil
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import Ollama

persist_directory = "db"

def process_pdf(file_bytes):
    # Clear old DB first
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load_and_split()

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(pages, embeddings, persist_directory=persist_directory)
    return True

def get_answer(query: str):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    retriever = vectorstore.as_retriever()

    # Use Ollama to run a local LLM like mistral
    local_llm = Ollama(model="mistral", temperature=0.0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=local_llm,
        retriever=retriever
    )

    return qa_chain.run(query)
