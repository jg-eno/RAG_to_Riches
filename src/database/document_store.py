"""Document storage and retrieval functionality."""
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os
import shutil

from src.config.settings import API_KEY, DEFAULT_DOC_PATH, DEFAULT_CHROMA_PATH, EMBEDDING_MODEL, get_document_db_path

# Global variable to cache database instances
_db_instances = {}

def load_document(path):
    """Load and split a PDF document into chunks."""
    print(f"Loading document from: {path}")
    doc_loader = PyPDFLoader(path)
    documents = doc_loader.load()
    print(f"Loaded {len(documents)} pages")
    
    # Optimize chunk size for better retrieval performance
    # Smaller chunks with moderate overlap for better semantic matching
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,  # Reduced from 1000 for more precise retrieval
        chunk_overlap=100,  # Reduced from 200 to minimize redundancy
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks

def initialize_database(doc_path=None):
    """Initialize and populate the vector database for a specific document."""
    global _db_instances
    
    # Use default document if none provided
    doc_path = doc_path or DEFAULT_DOC_PATH
    
    # Get document-specific database path
    db_path = get_document_db_path(doc_path)
    
    # Check if database already exists to avoid rebuilding
    if os.path.exists(db_path) and os.path.isdir(db_path) and len(os.listdir(db_path)) > 0:
        print(f"Using existing database at: {db_path}")
        db = get_database(doc_path)
        _db_instances[doc_path] = db
        return db
    
    # Ensure the database directory exists
    os.makedirs(db_path, exist_ok=True)
    
    documents = load_document(doc_path)
    
    embedding_function = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=API_KEY(),  # Call the function to get the next API key
        # Add caching to avoid redundant embedding calculations
        cache=True
    )
    
    print(f"Creating vector database at: {db_path}")
    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=db_path
    )
    print("Database created successfully")
    
    # Cache the database instance
    _db_instances[doc_path] = db
    return db

def get_database(doc_path=None):
    """Get an instance of the vector database for a specific document."""
    global _db_instances
    
    # Use default document if none provided
    doc_path = doc_path or DEFAULT_DOC_PATH
    
    # Return cached instance if available
    if doc_path in _db_instances:
        return _db_instances[doc_path]
    
    # Get document-specific database path
    db_path = get_document_db_path(doc_path)
    
    embedding_function = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=API_KEY(),  # Call the function to get the next API key
        # Add caching to avoid redundant embedding calculations
        cache=True
    )
    
    # Create and cache the database instance
    db = Chroma(persist_directory=db_path, embedding_function=embedding_function)
    _db_instances[doc_path] = db
    return db

def delete_database(doc_path):
    """Delete a document's vector database."""
    global _db_instances
    
    # Get document-specific database path
    db_path = get_document_db_path(doc_path)
    
    # Remove from cache if present
    if doc_path in _db_instances:
        del _db_instances[doc_path]
    
    # Delete the database directory if it exists
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
        print(f"Deleted database at: {db_path}")
        return True
    
    return False
