"""UI styles and CSS configurations."""

CUSTOM_CSS = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto;
    padding-top: 1.5rem !important;
    background: linear-gradient(to bottom right, #ffffff, #f5f5f5);
}

.chat-message {
    padding: 1rem;
    border-radius: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.chat-message:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.chat-message.user {
    background: #e3f2fd;
    border-bottom-right-radius: 0.2rem;
}

.chat-message.bot {
    background: #f3f4f6;
    border-bottom-left-radius: 0.2rem;
}

h1.gr-text-center {
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    margin-bottom: 1rem !important;
    background: linear-gradient(90deg, #2196F3, #1976D2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}

.gr-form {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 1rem;
    padding: 1rem;
    background: white;
}

.gr-button {
    border-radius: 0.5rem !important;
    transition: all 0.3s ease !important;
}

.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.gr-input {
    border-radius: 0.5rem !important;
    border: 2px solid #e0e0e0 !important;
    padding: 0.75rem !important;
    transition: all 0.3s ease !important;
}

.gr-input:focus {
    border-color: #2196F3 !important;
    box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.2) !important;
}

.examples {
    gap: 0.5rem !important;
}

.examples .gr-button {
    background: #f3f4f6 !important;
    border: 1px solid #e0e0e0 !important;
}

.examples .gr-button:hover {
    background: #e3f2fd !important;
    border-color: #2196F3 !important;
}
"""
