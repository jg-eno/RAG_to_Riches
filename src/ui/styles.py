"""Enhanced UI styles and CSS configurations for a professional dark futuristic interface."""

CUSTOM_CSS = """
/* Professional dark futuristic UI styling */
:root {
    --primary-color: #0084ff;
    --primary-dark: #0065d1;
    --primary-light: #00f2fe;
    --secondary-color: #3b82f6;
    --accent-color: #00e2ff;
    --text-color: #e2e8f0;
    --text-light: #94a3b8;
    --text-dark: #1e293b;
    --background-color: #121318;
    --bg-secondary: #1e1e24;
    --card-bg: rgba(15, 23, 42, 0.8);
    --card-border: rgba(30, 41, 59, 0.5);
    --border-radius: 12px;
    --box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    --glass-bg: rgba(15, 23, 42, 0.7);
    --glass-border: 1px solid rgba(30, 41, 59, 0.5);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    --glow-blue: 0 0 10px rgba(0, 132, 255, 0.5), 0 0 20px rgba(0, 132, 255, 0.3);
    --neon-glow: 0 0 5px #0084ff, 0 0 15px rgba(0, 132, 255, 0.8);
}

/* Full screen styles */
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow-x: hidden;
    background: var(--background-color);
    color: var(--text-color);
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

body {
    background: radial-gradient(circle at top right, #0c0f16, #121318 30%, #0f1117 70%);
    background-attachment: fixed;
}

.gradio-container {
    min-height: 100vh !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
    display: flex !important;
    flex-direction: column !important;
}

.fullscreen-container {
    max-width: 1600px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding: 0 2rem !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

.container {
    border-radius: var(--border-radius) !important;
    box-shadow: var(--glass-shadow) !important;
    overflow: hidden !important;
    background: var(--glass-bg) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border: var(--glass-border) !important;
}

/* Header styling */
h1.gr-text-center {
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    margin: 1.5rem 0 !important;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
    letter-spacing: -0.03em !important;
    text-shadow: var(--glow-blue) !important;
}

/* Description styling */
.description {
    background: rgba(15, 23, 42, 0.5) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-radius: var(--border-radius) !important;
    box-shadow: var(--glass-shadow) !important;
    padding: 1.25rem !important;
    margin-bottom: 1.25rem !important;
    border: 1px solid rgba(30, 41, 59, 0.3) !important;
    position: relative !important;
    overflow: hidden !important;
    color: var(--text-light) !important;
}

.description::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    box-shadow: var(--neon-glow);
}

.description-header {
    display: flex !important;
    align-items: center !important;
    margin-bottom: 1rem !important;
}

.header-icon {
    font-size: 1.5rem !important;
    margin-right: 0.75rem !important;
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-shadow: var(--glow-blue) !important;
}

.features-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 0.75rem !important;
    margin: 1rem 0 !important;
}

.feature {
    display: flex !important;
    align-items: center !important;
    padding: 0.6rem 0.8rem !important;
    background: rgba(30, 41, 59, 0.6) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    transition: var(--transition) !important;
}

.feature:hover {
    transform: translateY(-2px) !important;
    border-color: rgba(59, 130, 246, 0.5) !important;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(0, 132, 255, 0.2) !important;
}

.feature-icon {
    margin-right: 0.75rem !important;
    font-size: 1.25rem !important;
    color: var(--primary-color) !important;
}

.feature-text {
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    color: var(--text-color) !important;
}

/* Chat message styling - Full screen */
.fullscreen-chat {
    flex: 1 !important;
    min-height: 50vh !important;
    margin-bottom: 0.75rem !important;
}

.chat-container {
    border-radius: var(--border-radius) !important;
    background: rgba(15, 23, 42, 0.5) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    padding: 0.4rem !important;
    border: 1px solid var(--card-border) !important;
    box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.2) !important;
    font-size: 1.1rem !important;
}

.chat-message {
    padding: 1rem !important;
    border-radius: var(--border-radius) !important;
    margin-bottom: 0.75rem !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
    transition: var(--transition) !important;
    position: relative !important;
    overflow: hidden !important;
    backdrop-filter: blur(5px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
    border: 1px solid rgba(30, 41, 59, 0.3) !important;
    font-size: 1.1rem !important;
    line-height: 1.6 !important;
}

.chat-message::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    opacity: 0;
    transition: var(--transition);
}

.chat-message:hover {
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.25) !important;
    transform: translateY(-2px) !important;
}

.chat-message:hover::before {
    opacity: 1;
}

.chat-message.user {
    background: linear-gradient(135deg, rgba(0, 132, 255, 0.1) 0%, rgba(0, 132, 255, 0.05) 100%) !important;
    border-bottom-right-radius: 4px !important;
    border: 1px solid rgba(0, 132, 255, 0.2) !important;
}

.chat-message.bot {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.7) 100%) !important;
    border-bottom-left-radius: 4px !important;
    border: 1px solid rgba(30, 41, 59, 0.5) !important;
}

/* Avatar styling */
.avatar {
    border-radius: 12px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 42px !important;
    height: 42px !important;
    font-size: 1.25rem !important;
    margin-right: 12px !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
}

.avatar.user {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-dark)) !important;
    box-shadow: var(--glow-blue) !important;
}

.avatar.bot {
    background: linear-gradient(135deg, #334155, #1e293b) !important;
    border: 1px solid rgba(59, 130, 246, 0.3) !important;
}

/* Input styling - Full screen width */
.input-container {
    position: relative !important;
    margin-bottom: 0.75rem !important;
    border-radius: var(--border-radius) !important;
    background: rgba(15, 23, 42, 0.5) !important;
    border: 1px solid var(--card-border) !important;
    padding: 0.6rem !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
}

.dark-input {
    border-radius: var(--border-radius) !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    padding: 1rem !important;
    transition: var(--transition) !important;
    font-size: 1rem !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
    background: rgba(15, 23, 42, 0.7) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    color: var(--text-color) !important;
}

.dark-input:focus {
    border-color: var(--primary-color) !important;
    box-shadow: 0 0 0 3px rgba(0, 132, 255, 0.2), var(--glow-blue) !important;
    outline: none !important;
    background: rgba(15, 23, 42, 0.9) !important;
}

.dark-input::placeholder {
    color: var(--text-light) !important;
    letter-spacing: 0.01em !important;
}

/* Button styling */
.gr-button {
    border-radius: var(--border-radius) !important;
    transition: var(--transition) !important;
    font-weight: 600 !important;
    text-transform: none !important;
    letter-spacing: 0.02em !important;
    padding: 0.75rem 1.5rem !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
    border: none !important;
}

.gr-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25), var(--glow-blue) !important;
}

.neon-btn {
    background: linear-gradient(90deg, var(--primary-color), var(--primary-dark)) !important;
    color: white !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 0 5px rgba(0, 132, 255, 0.5), 0 0 15px rgba(0, 132, 255, 0.3) !important;
}

.neon-btn::after {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        to bottom right,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 0.1) 50%,
        rgba(255, 255, 255, 0) 100%
    );
    transform: rotate(45deg);
    animation: shine 6s infinite;
}

@keyframes shine {
    0% {
        transform: rotate(45deg) translateX(-100%);
    }
    20%, 100% {
        transform: rotate(45deg) translateX(100%);
    }
}

.gr-button-secondary {
    background: rgba(15, 23, 42, 0.8) !important;
    color: var(--primary-color) !important;
    border: 1px solid var(--primary-color) !important;
    backdrop-filter: blur(5px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
}

/* Examples styling */
.examples {
    gap: 0.75rem !important;
    margin-top: 1.25rem !important;
    margin-bottom: 1.75rem !important;
}

.examples .gr-button {
    background: rgba(15, 23, 42, 0.7) !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    color: var(--text-light) !important;
    font-size: 0.9rem !important;
    padding: 0.7rem 1.1rem !important;
    border-radius: var(--border-radius) !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
    backdrop-filter: blur(5px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
}

.examples .gr-button:hover {
    background: rgba(30, 41, 59, 0.9) !important;
    border-color: var(--primary-color) !important;
    color: var(--primary-color) !important;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2), var(--glow-blue) !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.5);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: rgba(59, 130, 246, 0.4);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(59, 130, 246, 0.7);
}

/* Markdown content styling */
.markdown-content h1, .markdown-content h2, .markdown-content h3 {
    color: var(--text-color) !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
    font-size: 1.4rem !important;
}

.markdown-content p {
    margin-bottom: 1rem !important;
    line-height: 1.7 !important;
    color: var(--text-light) !important;
    font-size: 1.15rem !important;
}

.markdown-content ul, .markdown-content ol {
    margin-bottom: 1rem !important;
    padding-left: 1.5rem !important;
    color: var(--text-light) !important;
    font-size: 1.15rem !important;
}

.markdown-content li {
    margin-bottom: 0.5rem !important;
    line-height: 1.6 !important;
    font-size: 1.15rem !important;
}

.markdown-content table {
    border-collapse: collapse !important;
    width: 100% !important;
    margin-bottom: 1.5rem !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
    background: rgba(15, 23, 42, 0.5) !important;
    backdrop-filter: blur(5px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
    font-size: 1.1rem !important;
}

.markdown-content th {
    background-color: rgba(30, 41, 59, 0.8) !important;
    padding: 0.875rem 1.25rem !important;
    text-align: left !important;
    font-weight: 600 !important;
    color: var(--text-color) !important;
    border-bottom: 2px solid #334155 !important;
    position: relative !important;
    font-size: 1.15rem !important;
}

.markdown-content th::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    opacity: 0.6;
}

.markdown-content td {
    padding: 0.875rem 1.25rem !important;
    border-bottom: 1px solid rgba(59, 130, 246, 0.1) !important;
    color: var(--text-light) !important;
    font-size: 1.1rem !important;
}

.markdown-content tr:last-child td {
    border-bottom: none !important;
}

.markdown-content tr:nth-child(even) {
    background-color: rgba(30, 41, 59, 0.3) !important;
}

.markdown-content code {
    background-color: rgba(30, 41, 59, 0.7) !important;
    padding: 0.2rem 0.4rem !important;
    border-radius: 4px !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 1rem !important;
    color: #00f2fe !important;
}

.markdown-content pre {
    background-color: rgba(15, 23, 42, 0.95) !important;
    color: #e2e8f0 !important;
    padding: 1.25rem !important;
    border-radius: 8px !important;
    overflow-x: auto !important;
    margin-bottom: 1.25rem !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    font-size: 1.05rem !important;
}

.markdown-content pre code {
    background-color: transparent !important;
    color: #00f2fe !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

.markdown-content blockquote {
    border-left: 4px solid var(--primary-color) !important;
    padding: 0.75rem 1.25rem !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    font-style: italic !important;
    color: var(--text-light) !important;
    background: rgba(15, 23, 42, 0.5) !important;
    border-radius: 0 8px 8px 0 !important;
}

/* Footer styling */
.footer {
    margin-top: 2.5rem !important;
    padding: 1.5rem !important;
    border-top: 1px solid rgba(59, 130, 246, 0.2) !important;
    background: rgba(15, 23, 42, 0.3) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
}

.footer-content {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-bottom: 1rem !important;
}

.footer-logo {
    font-weight: 800 !important;
    font-size: 1.2rem !important;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    letter-spacing: -0.02em !important;
    text-shadow: var(--glow-blue) !important;
}

.footer-divider {
    width: 1px !important;
    height: 1.5rem !important;
    background-color: rgba(59, 130, 246, 0.3) !important;
    margin: 0 1rem !important;
}

.footer-text {
    color: var(--text-light) !important;
    font-size: 0.875rem !important;
}

.footer-line {
    height: 4px !important;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
    width: 100px !important;
    margin: 0 auto !important;
    border-radius: 2px !important;
    opacity: 0.6 !important;
    box-shadow: var(--neon-glow) !important;
}

/* Loading animation */
.loading {
    position: relative !important;
}

.loading::after {
    content: "" !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 3px !important;
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light), var(--primary-color)) !important;
    background-size: 300% 100% !important;
    animation: loading-animation 2s linear infinite !important;
    box-shadow: var(--neon-glow) !important;
}

@keyframes loading-animation {
    0% {
        background-position: 0% 50%;
    }
    20%, 100% {
        background-position: 300% 50%;
    }
}
"""