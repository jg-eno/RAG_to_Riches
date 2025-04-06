"""Configuration settings for the application."""
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API and path configurations
API_KEY = os.getenv('GEMINI_API_KEY')
DOC_PATH = os.getenv('DOC_PATH')
CHROMA_PATH = os.getenv('CHROMA_PATH')

# Model configurations
GEMINI_MODEL = 'gemini-2.5-pro-exp-03-25'
EMBEDDING_MODEL = 'models/text-embedding-004'

# Validate required environment variables
if not all([API_KEY, DOC_PATH, CHROMA_PATH]):
    raise ValueError("Missing required environment variables. Please check your .env file")
