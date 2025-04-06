"""Document storage and retrieval functionality."""
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from src.config.settings import API_KEY, DOC_PATH, CHROMA_PATH, EMBEDDING_MODEL

def load_document(path):
    """Load and split a PDF document into chunks."""
    print(f"Loading document from: {path}")
    doc_loader = PyPDFLoader(path)
    documents = doc_loader.load()
    print(f"Loaded {len(documents)} pages")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks

def initialize_database():
    """Initialize and populate the vector database."""
    documents = load_document(DOC_PATH)
    
    embedding_function = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=API_KEY
    )
    
    print(f"Creating vector database at: {CHROMA_PATH}")
    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=CHROMA_PATH
    )
    print("Database created successfully")
    return db

def get_database():
    """Get an instance of the vector database."""
    embedding_function = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=API_KEY
    )
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
