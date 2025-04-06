"""Main entry point for the application."""
from src.database.document_store import initialize_database
from src.ui.app import create_chat_interface
from src.config.settings import DEFAULT_DOC_PATH

def main():
    """Initialize the database and launch the chat interface."""
    # Initialize the database with the default document
    initialize_database(DEFAULT_DOC_PATH)
    
    # Create and launch the chat interface
    app = create_chat_interface()
    app.launch(debug=True,share=True)

if __name__ == "__main__":
    main()