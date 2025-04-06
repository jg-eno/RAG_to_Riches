"""UI components and layout for the chat interface."""
import gradio as gr
import os
import tempfile
import time
import shutil

from src.utils.query_handler import chat_response
from src.ui.styles import CUSTOM_CSS
from src.database.document_store import initialize_database, delete_database
from src.config.settings import UPLOAD_FOLDER, DEFAULT_DOC_PATH

def create_chat_interface():
    """Create and configure the professional dark futuristic chat interface."""
    # Get the absolute paths to the avatar SVG files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_avatar = os.path.join(current_dir, "assets", "user_avatar.svg")
    assistant_avatar = os.path.join(current_dir, "assets", "assistant_avatar.svg")
    
    # Dark futuristic theme with neon blue accents
    theme = gr.themes.Base(
        primary_hue="blue",
        secondary_hue="indigo",
        neutral_hue="slate",
        font=("Inter", "system-ui"),
        radius_size=gr.themes.sizes.radius_md,
    ).set(
        button_primary_background_fill="linear-gradient(90deg, #0084ff, #00f2fe)",
        button_primary_background_fill_hover="linear-gradient(90deg, #0077e6, #00d8e6)",
        button_primary_text_color="white",
        button_secondary_background_fill="rgba(30, 41, 59, 0.8)",
        button_secondary_background_fill_hover="rgba(30, 41, 59, 0.9)",
        button_secondary_text_color="#0084ff",
        button_secondary_border_color="#0084ff",
        background_fill_primary="#121318",
        block_background_fill="rgba(15, 23, 42, 0.8)",
        block_label_background_fill="rgba(30, 41, 59, 0.7)",
        block_label_text_color="#94a3b8",
        block_title_text_color="#e2e8f0",
        block_border_width="0",
        block_shadow="0 10px 25px -5px rgb(0 0 0 / 0.3), 0 8px 10px -6px rgb(0 0 0 / 0.3)",
    )
    
    # Enhanced header with dark futuristic design
    header = gr.HTML("""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 2rem;">
            <div style="text-align: center;">
                <h1 style="margin-bottom: 0.75rem; font-size: 2.75rem; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient(90deg, #0084ff, #00f2fe); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">InsiderInfo</h1>
                <h2 style="margin-top: 0; margin-bottom: 0.75rem; font-size: 1.5rem; font-weight: 700; color: #e2e8f0;">A Single Document RAG based ChatBot</h2>
                <div style="width: 120px; height: 4px; background: linear-gradient(90deg, #0084ff, #00f2fe); margin: 0 auto 1.5rem;"></div>
                <p style="font-size: 1.1rem; color: #94a3b8; max-width: 800px; margin: 0 auto; line-height: 1.6;">
                    Single-document chat: Interaction with an individual document. Activity given by Ailaysa
                </p>
                <p>By J Glen Enosh</p>
            </div>
        </div>
    """)
    
    # Function to handle PDF uploads
    def handle_upload(file):
        if file is None:
            return None, gr.update(visible=False), gr.update(visible=True), "No file uploaded"
        
        # Create a unique filename to avoid conflicts
        timestamp = int(time.time())
        filename = f"{timestamp}_{os.path.basename(file.name)}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Save the uploaded file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        shutil.copy(file.name, file_path)
        
        # Initialize the database for this document
        try:
            initialize_database(file_path)
            return file_path, gr.update(visible=True), gr.update(visible=False), f"Successfully uploaded and processed: {os.path.basename(file_path)}"
        except Exception as e:
            return None, gr.update(visible=False), gr.update(visible=True), f"Error processing document: {str(e)}"
    
    # Function to handle document-specific chat
    def document_chat(message, history, active_document):
        if not active_document:
            return "", history + [
                {"role": "user", "content": message},
                {"role": "assistant", "content": "Please upload a document first before asking questions."}
            ]
        
        return chat_response(message, history, active_document)
    
    # Create the interface with full-screen dark styling
    with gr.Blocks(theme=theme, css=CUSTOM_CSS) as app:
        header.render()
        
        # State for tracking the active document
        active_document = gr.State(DEFAULT_DOC_PATH)
        
        # Using Column instead of Box with enhanced design
        with gr.Column(elem_classes=["container", "fullscreen-container"]):
            # Document upload section
            with gr.Column(elem_classes=["description"]):
                gr.Markdown("""
                <div class="description-header">
                    <div class="header-icon">📄</div>
                    <h3 style="margin-top: 0; color: #0084ff; font-weight: 700; letter-spacing: -0.01em;">DOCUMENT MANAGEMENT</h3>
                </div>
                <p>Upload your own PDF document to analyze or use the default document.</p>
                """)
                
                with gr.Row():
                    file_upload = gr.File(
                        label="Upload PDF Document",
                        file_types=[".pdf"],
                        elem_classes=["file-upload"]
                    )
                    
                upload_status = gr.Textbox(
                    label="Upload Status",
                    interactive=False,
                    elem_classes=["status-box"]
                )
                
                with gr.Row(visible=False) as active_doc_row:
                    active_doc_display = gr.Textbox(
                        label="Active Document",
                        interactive=False,
                        elem_classes=["active-doc"]
                    )
                    reset_btn = gr.Button("Use Default Document", variant="secondary")
                
                with gr.Row(visible=True) as default_doc_row:
                    gr.Markdown(f"""
                    <div style="padding: 0.5rem; background: rgba(30, 41, 59, 0.6); border-radius: 8px; text-align: center;">
                        Currently using the default document: <span style="color: #0084ff; font-weight: 600;">{os.path.basename(DEFAULT_DOC_PATH)}</span>
                    </div>
                    """)
            
            gr.Markdown("""
            <div class="description">
                <div class="description-header">
                    <div class="header-icon">🔍</div>
                    <h3 style="margin-top: 0; color: #0084ff; font-weight: 700; letter-spacing: -0.01em;">SYSTEM CAPABILITIES</h3>
                </div>
                <p>Engage and Interact with GPT-4_VS_Human_translators.pdf </p>
                <div class="features-grid">
                    <div class="feature">
                        <div class="feature-icon">📊</div>
                        <div class="feature-text">Accurate Data Retrieval</div>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">🔄</div>
                        <div class="feature-text">Contextual understanding</div>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">📋</div>
                        <div class="feature-text">Structured Response</div>
                    </div>
                </div>
                <p style="margin-bottom: 0; font-size: 0.9rem; color: #94a3b8;">Optimize results by formulating precise queries related to document content.</p>
            </div>
            """)
            
            # Enhanced chatbot UI with full-screen dark design
            chatbot = gr.Chatbot(
                height="50vh",  # Reduced height from 65vh to 50vh
                show_label=False,
                avatar_images=(user_avatar, assistant_avatar),
                type="messages",
                elem_classes=["chat-container", "fullscreen-chat"],
                bubble_full_width=False
            )
            
            with gr.Row(elem_classes=["input-container"]):
                with gr.Column(scale=20):
                    msg = gr.Textbox(
                        placeholder="Enter your query for document analysis...",
                        container=False,
                        scale=7,
                        min_width=600,
                        show_label=False,
                        elem_classes=["chat-input", "dark-input"]
                    )
                with gr.Column(scale=1, min_width=70):
                    submit_btn = gr.Button("Process", variant="primary", elem_classes=["send-btn", "neon-btn"])
            
            with gr.Row(elem_classes=["examples-container"]):
                gr.Examples(
                    examples=[
                        "Analyze the primary findings and conclusions of this document",
                        "Extract and organize the key methodological approaches",
                        "Generate a comparative analysis of the frameworks discussed"
                    ],
                    inputs=msg,
                    label="Example Queries"
                )
        
        # Event handlers
        file_upload.upload(
            handle_upload,
            inputs=[file_upload],
            outputs=[active_document, active_doc_row, default_doc_row, upload_status]
        )
        
        file_upload.change(
            handle_upload,
            inputs=[file_upload],
            outputs=[active_document, active_doc_row, default_doc_row, upload_status]
        )
        
        def update_active_doc_display(doc_path):
            return os.path.basename(doc_path) if doc_path else "No document selected"
        
        active_document.change(
            update_active_doc_display,
            inputs=[active_document],
            outputs=[active_doc_display]
        )
        
        def reset_to_default():
            return DEFAULT_DOC_PATH, gr.update(visible=False), gr.update(visible=True), "Reset to default document"
        
        reset_btn.click(
            reset_to_default,
            outputs=[active_document, active_doc_row, default_doc_row, upload_status]
        )
        
        # Message submission
        submit_btn.click(
            document_chat,
            inputs=[msg, chatbot, active_document],
            outputs=[msg, chatbot]
        )
        
        msg.submit(
            document_chat,
            inputs=[msg, chatbot, active_document],
            outputs=[msg, chatbot]
        )
    
    return app