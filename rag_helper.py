from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.llms.ollama import Ollama
import tempfile

def ask_rag_qa(query, uploaded_files):
    all_docs = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            loader = PyPDFLoader(tmp.name)
            docs = loader.load()
            all_docs.extend(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(all_docs, embeddings)
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=Ollama(model="tinyllama"), retriever=retriever)
    return qa_chain.run(query)
