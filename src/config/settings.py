"""Configuration settings for the application."""
import os
from dotenv import load_dotenv
from src.utils.api_load_balancer import get_api_key

# Load environment variables
load_dotenv()

# API and model configuration
API_KEY = get_api_key  # Now a function that returns the next API key
GEMINI_MODEL = "gemini-2.5-pro-preview-03-25"
EMBEDDING_MODEL = "models/text-embedding-004"

# Default document and database paths
DEFAULT_DOC_PATH = os.getenv("DOC_PATH", "documents/GPT-4_VS_Human_translators.pdf")
DEFAULT_CHROMA_PATH = os.getenv("CHROMA_PATH", "chroma")

# Uploaded documents directory
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to get document-specific database path
def get_document_db_path(doc_name):
    """Get a unique database path for a specific document."""
    # Create a safe filename for the database
    safe_name = os.path.splitext(os.path.basename(doc_name))[0]
    safe_name = "".join(c if c.isalnum() else "_" for c in safe_name)
    return os.path.join(DEFAULT_CHROMA_PATH, safe_name)
