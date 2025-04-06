"""Main entry point for the Document Q&A application."""
from src.database.document_store import initialize_database
from src.ui.app import create_chat_interface
from src.ui.styles import CUSTOM_CSS

def main():
    # Initialize the document database
    print("Initializing document database...")
    initialize_database()

    # Create and launch the chat interface
    app = create_chat_interface()
    app.queue()
    app.launch(css=CUSTOM_CSS)

if __name__ == "__main__":
    main()