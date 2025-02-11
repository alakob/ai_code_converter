"""Configuration settings for the AI Code Converter application."""

# Model configurations
OPENAI_MODEL = "gpt-4o-mini"
CLAUDE_MODEL = "claude-3-sonnet-20240307"
DEEPSEEK_MODEL = "deepseek-chat"
GEMINI_MODEL = "gemini-1.5-flash"
GROQ_MODEL = "llama3-70b-8192"

# Supported languages and models
SUPPORTED_LANGUAGES = ["Python", "Julia", "JavaScript", "Go", "Java", "C++"]
MODELS = ["GPT", "Claude", "Gemini", "DeepSeek", "GROQ"]

# Language mapping for syntax highlighting
LANGUAGE_MAPPING = {
    "Python": "python",
    "JavaScript": "javascript",
    "Java": "python",
    "C++": "cpp",
    "Julia": "python",
    "Go": "c"
}

# CSS styling
CUSTOM_CSS = """
.code-container {
    height: 30vh;
    overflow: auto;
    border-radius: 4px;
    scrollbar-width: none;
    -ms-overflow-style: none;
}

.code-container::-webkit-scrollbar {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    background: transparent !important;
}

.code-container .scroll-hide::-webkit-scrollbar,
.code-container > div::-webkit-scrollbar,
.code-container textarea::-webkit-scrollbar,
.code-container pre::-webkit-scrollbar,
.code-container code::-webkit-scrollbar {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    background: transparent !important;
}

.code-container .language-select {
    overflow: auto !important;
    max-height: 100% !important;
}

.accordion {
    margin-top: 1rem !important;
}

.error-accordion {
    margin: 10px 0;
    border: 2px solid #ff4444 !important;
    border-radius: 4px !important;
    background-color: #2b2b2b !important;
}

.error-message {
    color: #ff4444;
    font-weight: bold;
    font-size: 16px;
    padding: 10px;
}

.gradio-container {
    padding-top: 1rem;
}

.header-text {
    text-align: center;
    font-size: 2rem;
    font-color: #283042;
    font-weight: bold;
    margin-bottom: 1rem;
}
""" 