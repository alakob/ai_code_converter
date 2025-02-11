"""Module for detecting programming languages in code snippets."""

import re
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

class LanguageDetector:
    """Class for detecting programming languages in code snippets."""
    
    @staticmethod
    def detect_python(code: str) -> bool:
        """Detect if code is Python."""
        patterns = [
            r'def\s+\w+\s*\([^)]*\)\s*:',  # Function definition
            r'import\s+[\w\s,]+',           # Import statements
            r'from\s+[\w.]+\s+import',      # From import statements
            r'print\s*\([^)]*\)',           # Print statements
            r':\s*$'                        # Line ending with colon
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_javascript(code: str) -> bool:
        """Detect if code is JavaScript."""
        patterns = [
            r'function\s+\w+\s*\([^)]*\)',  # Function declaration
            r'const\s+\w+\s*=',             # Const declaration
            r'let\s+\w+\s*=',               # Let declaration
            r'var\s+\w+\s*=',               # Var declaration
            r'console\.(log|error|warn)'    # Console methods
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_java(code: str) -> bool:
        """Detect if code is Java."""
        patterns = [
            r'public\s+class\s+\w+',        # Class declaration
            r'public\s+static\s+void\s+main', # Main method
            r'System\.(out|err)\.',         # System output
            r'private|protected|public',     # Access modifiers
            r'import\s+java\.'              # Java imports
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_cpp(code: str) -> bool:
        """Detect if code is C++."""
        patterns = [
            r'#include\s*<[^>]+>',          # Include statements
            r'std::\w+',                    # STD namespace usage
            r'cout\s*<<',                   # Console output
            r'cin\s*>>',                    # Console input
            r'int\s+main\s*\('              # Main function
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_julia(code: str) -> bool:
        """Detect if code is Julia."""
        patterns = [
            r'function\s+\w+\s*\([^)]*\)\s*end', # Function with end
            r'println\(',                   # Print function
            r'using\s+\w+',                # Using statement
            r'module\s+\w+',               # Module declaration
            r'struct\s+\w+'                # Struct declaration
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_go(code: str) -> bool:
        """Detect if code is Go."""
        patterns = [
            r'package\s+\w+',              # Package declaration
            r'func\s+\w+\s*\(',            # Function declaration
            r'import\s*\(',                # Import block
            r'fmt\.',                      # fmt package usage
            r'type\s+\w+\s+struct'         # Struct declaration
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    def __init__(self):
        """Initialize language detector with detection functions."""
        self.detectors = {
            "Python": self.detect_python,
            "JavaScript": self.detect_javascript,
            "Java": self.detect_java,
            "C++": self.detect_cpp,
            "Julia": self.detect_julia,
            "Go": self.detect_go
        }

    def detect_language(self, code: str) -> str:
        """
        Detect the programming language of the given code.
        
        Args:
            code: Code snippet to analyze
            
        Returns:
            Detected language name or None if unknown
        """
        for lang, detector in self.detectors.items():
            if detector(code):
                return lang
        return None

    def validate_language(self, code: str, expected_lang: str) -> tuple[bool, str]:
        """Validate if code matches the expected programming language."""
        logger = logging.getLogger(__name__)
        
        logger.info(f"Starting code validation for {expected_lang}")
        logger.info(f"Code length: {len(code)} characters")
        
        if not code or not expected_lang:
            logger.warning("Empty code or language not specified")
            return True, ""
        
        detector = self.detectors.get(expected_lang)
        if not detector:
            logger.warning(f"No detector found for language: {expected_lang}")
            return True, ""
        
        if detector(code):
            logger.info(f"Code successfully validated as {expected_lang}")
            return True, ""
        
        detected_lang = self.detect_language(code)
        error_msg = f"Code appears to be {detected_lang or 'unknown'} but {expected_lang} was selected"
        logger.error(f"Language validation failed: {error_msg}")
        return False, error_msg 