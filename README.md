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

## Quick Start

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

## Basic Usage

1. Select source and target programming languages
2. Enter or upload source code
3. Choose AI model and temperature
4. Click "Convert" to translate the code
5. Use "Run" buttons to execute original or converted code
6. Download the results including compiled binaries (for compiled languages)

## Supported Languages

Currently supports 17 programming languages including Python, JavaScript, Java, C++, Julia, Go, Ruby, Swift, Rust, C#, TypeScript, R, Perl, Lua, PHP, Kotlin, and SQL.

See [Supported Languages](./docs/languages.md) for detailed information on each language.

## Documentation

For detailed documentation, please refer to the [docs](./docs) directory:

- [Supported Languages](./docs/languages.md) - Details on all supported programming languages
- [Configuration Guide](./docs/configuration.md) - How to configure the application
- [Development Guide](./docs/development.md) - Guide for developers extending the application
- [Contributing Guidelines](./docs/contributing.md) - How to contribute to the project
- [Project Structure](./docs/project_structure.md) - Overview of the codebase architecture

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude
- Google for Gemini
- DeepSeek and GROQ for their AI models
- The Gradio team for the web interface framework 