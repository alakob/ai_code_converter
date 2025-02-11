"""Module for handling AI model streaming responses."""

import logging
from typing import Generator
import anthropic
import google.generativeai as genai
from openai import OpenAI

from src.ai_code_converter.config import (
    OPENAI_MODEL,
    CLAUDE_MODEL,
    DEEPSEEK_MODEL,
    GEMINI_MODEL,
    GROQ_MODEL
)

logger = logging.getLogger(__name__)

class AIModelStreamer:
    """Class for handling streaming responses from various AI models."""
    
    def __init__(self, openai_client: OpenAI, claude_client: anthropic.Anthropic,
                 deepseek_client: OpenAI, groq_client: OpenAI, gemini_model: genai.GenerativeModel):
        """Initialize with AI model clients."""
        self.openai = openai_client
        self.claude = claude_client
        self.deepseek = deepseek_client
        self.groq = groq_client
        self.gemini = gemini_model

    def stream_gpt(self, prompt: str) -> Generator[str, None, None]:
        """Stream responses from GPT model."""
        try:
            messages = [{"role": "user", "content": prompt}]
            stream = self.openai.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                stream=True
            )
            
            response = ""
            for chunk in stream:
                fragment = chunk.choices[0].delta.content or ""
                response += fragment
                yield response
                
        except Exception as e:
            logger.error(f"GPT API error: {str(e)}", exc_info=True)
            yield f"Error with GPT API: {str(e)}"

    def stream_claude(self, prompt: str) -> Generator[str, None, None]:
        """Stream responses from Claude model."""
        try:
            result = self.claude.messages.stream(
                model=CLAUDE_MODEL,
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response = ""
            with result as stream:
                for text in stream.text_stream:
                    response += text
                    yield response
                    
        except Exception as e:
            logger.error(f"Claude API error: {str(e)}", exc_info=True)
            yield f"Error with Claude API: {str(e)}"

    def stream_deepseek(self, prompt: str) -> Generator[str, None, None]:
        """Stream responses from DeepSeek model."""
        try:
            messages = [{"role": "user", "content": prompt}]
            stream = self.deepseek.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=messages,
                stream=True,
                temperature=0.7,
                max_tokens=4000
            )
            
            reply = ""
            for chunk in stream:
                fragment = chunk.choices[0].delta.content or ""
                reply += fragment
                yield reply
                
        except Exception as e:
            logger.error(f"DeepSeek API error: {str(e)}", exc_info=True)
            yield f"Error with DeepSeek API: {str(e)}"

    def stream_groq(self, prompt: str) -> Generator[str, None, None]:
        """Stream responses from GROQ model."""
        try:
            messages = [{"role": "user", "content": prompt}]
            stream = self.groq.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                stream=True,
                temperature=0.7,
                max_tokens=4000
            )
            
            reply = ""
            for chunk in stream:
                fragment = chunk.choices[0].delta.content or ""
                reply += fragment
                yield reply
                
        except Exception as e:
            logger.error(f"GROQ API error: {str(e)}", exc_info=True)
            yield f"Error with GROQ API: {str(e)}"

    def stream_gemini(self, prompt: str) -> Generator[str, None, None]:
        """Stream responses from Gemini model."""
        try:
            response = self.gemini.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 1,
                    "top_k": 1,
                    "max_output_tokens": 4000,
                },
                stream=True
            )
            
            reply = ""
            for chunk in response:
                if chunk.text:
                    reply += chunk.text
                    yield reply
                    
        except Exception as e:
            logger.error(f"Gemini API error: {str(e)}", exc_info=True)
            yield f"Error with Gemini API: {str(e)}" 