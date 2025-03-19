# CodeXchange AI

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A powerful tool for converting and executing code between different programming languages using AI models.

## Overview

AI Code Converter is a Python application that leverages various AI models to translate code between programming languages while maintaining functionality and idiomatic patterns.

### Key Features

- Multi-language code conversion
- Real-time code execution
- Multiple AI model support (GPT, Claude, DeepSeek, GROQ, Gemini)
- File upload/download functionality
- Syntax highlighting
- Detailed logging system
- Docker support

### Supported Languages

- Python
- JavaScript
- Java
- C++
- Julia
- Go

## Installation

### Prerequisites

- Python 3.10+
- Node.js
- Java JDK 17+
- Julia 1.9+
- Go 1.21+
- GCC/G++

### Using Docker (Recommended)

```bash
# Clone the repository
git clone git@github.com:alakob/ai_code_converter.git
cd ai_code_converter

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Build and run
docker compose up -d --build
```

The application will be available at `http://localhost:7860`

### Manual Installation

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the application
python run.py
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
DEEPSEEK_API_KEY=your_deepseek_key_here
GROQ_API_KEY=your_groq_key_here
PORT=7860  # Optional, default port for the web interface
```

### Model Configuration

Model names are configured in `src/ai_code_converter/config.py`:

```python
# Model configurations
OPENAI_MODEL = "gpt-4o-mini"              # OpenAI model name
CLAUDE_MODEL = "claude-3-sonnet-20240307" # Anthropic Claude model
DEEPSEEK_MODEL = "deepseek-chat"          # DeepSeek model
GEMINI_MODEL = "gemini-1.5-flash"         # Google Gemini model
GROQ_MODEL = "llama3-70b-8192"           # GROQ model
```

## Usage

1. Select source and target programming languages
2. Enter or upload source code
3. Choose AI model and temperature
4. Click "Convert" to translate the code
5. Use "Run" buttons to execute original or converted code
6. Download the results including compiled binaries (for compiled languages)

## Project Structure

```
ai_converter_v2/
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── run.py                 # Application entry point
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .env.example           # Environment variables template
└── src/                   # Source code directory
    └── ai_code_converter/
        ├── main.py        # Main application logic
        ├── app.py         # Gradio interface setup
        ├── config.py      # Model and app configuration
        ├── template.j2    # Prompt template
        ├── core/          # Core functionality
        ├── models/        # AI model integration
        └── utils/         # Utility functions
```

## Development

### Adding New Programming Languages

1. Update Language Configuration (`config.py`):
```python
SUPPORTED_LANGUAGES = [..., "NewLanguage"]
LANGUAGE_MAPPING = {..., "NewLanguage": "language_highlight_name"}
```

2. Add Language Detection (`core/language_detection.py`):
```python
class LanguageDetector:
    @staticmethod
    def detect_new_language(code: str) -> bool:
        patterns = [r'pattern1', r'pattern2', r'pattern3']
        return any(re.search(pattern, code) for pattern in patterns)
```

3. Add Execution Support (`core/code_execution.py`):
```python
def execute_new_language(self, code: str) -> tuple[str, Optional[bytes]]:
    with tempfile.NamedTemporaryFile(suffix='.ext', mode='w', delete=False) as f:
        f.write(code)
        file_path = f.name
    try:
        result = subprocess.run(
            ["compiler/interpreter", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout, None
    except Exception as e:
        return f"Error: {str(e)}", None
```

### Adding New AI Models

1. Update Model Configuration (`config.py`):
```python
NEW_MODEL = "model-name-version"
MODELS = [..., "NewModel"]
```

2. Add Model Integration (`models/ai_streaming.py`):
```python
def stream_new_model(self, prompt: str) -> Generator[str, None, None]:
    try:
        response = self.new_model_client.generate(
            prompt=prompt,
            stream=True
        )
        reply = ""
        for chunk in response:
            fragment = chunk.text
            reply += fragment
            yield reply
    except Exception as e:
        logger.error(f"New Model API error: {str(e)}", exc_info=True)
        yield f"Error with New Model API: {str(e)}"
```

### Testing

1. Add test cases for new components
2. Test language detection with sample code
3. Test code execution with various examples
4. Test model streaming with different prompts
5. Verify error handling and edge cases

### Logging

- JSON formatted logs with timestamps
- Stored in `logs` directory
- Separate console and file logging
- Detailed execution metrics

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Best Practices

- Follow existing patterns for consistency
- Add comprehensive error handling
- Include detailed logging
- Update documentation
- Add type hints for all new functions
- Follow PEP 8 style guidelines
- Test thoroughly before submitting changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude
- Google for Gemini
- DeepSeek and GROQ for their AI models
- The Gradio team for the web interface framework 