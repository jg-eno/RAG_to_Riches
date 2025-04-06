"""Main Gradio application interface."""
import gradio as gr
from src.utils.query_handler import chat_response
from src.ui.styles import CUSTOM_CSS

def create_chat_interface():
    """Create and configure the chat interface."""
    return gr.ChatInterface(
        fn=chat_response,
        title="📚 Document Q&A Assistant",
        description="""
        <div style='text-align: center; margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 0.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <p style='font-size: 1.1rem; color: #666;'>Ask questions about the document and get AI-powered answers with structured formatting.</p>
            <p style='font-size: 0.9rem; color: #888;'>The assistant will provide well-organized responses using tables, bullet points, and formatted text.</p>
        </div>
        """,
        examples=[
            "What are the main findings of this document?",
            "Can you summarize the key points?",
            "What methodology was used in this study?"
        ],
        theme="soft",
        chatbot=gr.Chatbot(
            height=600,
            show_label=False,
            avatar_images=("👤", "🤖"),
            type="messages",
            container=True,
            bubble_full_width=False
        ),
        textbox=gr.Textbox(
            placeholder="Ask me anything about the document...",
            container=False,
            scale=7,
            min_width=600
        )
    )
