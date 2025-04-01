"""Main entry point for the CodeXchange AI application."""

import os
import sys
import traceback
from src.ai_code_converter.app import CodeConverterApp
from src.ai_code_converter.utils.logger import setup_logger

def main():
    """Initialize and run the application."""
    # Initialize logger
    logger = setup_logger("ai_code_converter.main")
    
    try:
        logger.info("="*50)
        logger.info("Starting CodeXchange AI")
        logger.info("="*50)
        
        # Log environment information
        logger.info(f"Python version: {sys.version}")
        logger.info(f"Running on: {sys.platform}")
        logger.info(f"Current directory: {os.getcwd()}")
        logger.info(f"Script path: {__file__}")
        
        # Log package dependencies
        try:
            logger.info("Checking for required packages...")
            import gradio
            logger.info(f"Gradio version: {gradio.__version__}")
            
            try:
                import google.generativeai as genai
                logger.info(f"Google Generative AI package found")
            except ImportError:
                logger.error("Missing required package: google.generativeai")
                logger.info("To install: pip install google-generativeai")
                raise ImportError("Missing required package: google.generativeai. Please install with: pip install google-generativeai")
                
            # Check other critical dependencies
            import anthropic
            logger.info(f"Anthropic package found")
            
        except ImportError as e:
            logger.error(f"Missing required package: {str(e)}")
            raise
        
        logger.info("Initializing application components")
        app = CodeConverterApp()
        
        logger.info("Starting Gradio interface")
        app.run(share=True)
        
    except Exception as e:
        logger.error("Application failed to start", exc_info=True)
        logger.error(f"Error details: {type(e).__name__}: {str(e)}")
        logger.error(f"Stack trace: {traceback.format_exc()}")
        raise
    finally:
        logger.info("="*50)
        logger.info("Application shutdown")
        logger.info("="*50)

if __name__ == "__main__":
    main() 