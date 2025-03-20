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

    @staticmethod
    def detect_ruby(code: str) -> bool:
        """Detect if code is Ruby."""
        patterns = [
            r'def\s+\w+\s*(?:\([^)]*\))?\s*$', # Method definition without end
            r'class\s+\w+(?:\s*<\s*\w+)?\s*$', # Class definition without end
            r'require\s+["\']\w+["\']',    # Require statement
            r'\b(?:puts|print)\s',          # Output methods
            r'\bdo\s*\|[^|]*\|',            # Block with parameters
            r'\bend\b',                    # End keyword
            r':[a-zA-Z_]\w*\s*=>',          # Symbol hash syntax
            r'[a-zA-Z_]\w*:\s*[^,\s]'      # New hash syntax
        ]
        return any(re.search(pattern, code) for pattern in patterns)
        
    @staticmethod
    def detect_swift(code: str) -> bool:
        """Detect if code is Swift."""
        patterns = [
            r'import\s+(?:Foundation|UIKit|SwiftUI)',  # Common Swift imports
            r'(?:var|let)\s+\w+\s*:\s*\w+',         # Variable declaration with type
            r'func\s+\w+\s*\([^)]*\)\s*(?:->\s*\w+)?\s*\{',  # Function declaration
            r'class\s+\w+(?:\s*:\s*\w+)?\s*\{',    # Class declaration
            r'struct\s+\w+\s*\{',                    # Struct declaration
            r'@IBOutlet|@IBAction',                    # iOS annotations
            r'guard\s+let',                            # Guard statement
            r'if\s+let|if\s+var',                      # Optional binding
            r'override\s+func'                         # Method override
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    @staticmethod
    def detect_rust(code: str) -> bool:
        """Detect if code is Rust."""
        patterns = [
            r'fn\s+\w+\s*\([^)]*\)\s*(?:->\s*[^{]+)?\s*\{',  # Function declaration
            r'let\s+mut\s+\w+',              # Mutable variable declaration
            r'struct\s+\w+\s*\{[^}]*\}',    # Struct definition
            r'impl\s+\w+(?:\s+for\s+\w+)?', # Implementation block
            r'use\s+[\w:]+',                 # Import/use statement
            r'pub\s+(?:fn|struct|enum|mod)',  # Public items
            r'Vec<[^>]+>',                   # Vec generic type
            r'match\s+\w+\s*\{',             # Match expression
            r'#\[\w+(?:\([^)]*\))?\]'        # Attribute macros
        ]
        return any(re.search(pattern, code) for pattern in patterns)
        
    @staticmethod
    def detect_csharp(code: str) -> bool:
        """Detect if code is C#."""
        patterns = [
            r'using\s+[\w.]+;',                    # Using statement
            r'namespace\s+[\w.]+',                 # Namespace declaration
            r'(public|private|protected|internal)\s+(class|struct|interface|enum)',  # Type declarations
            r'(public|private|protected|internal)\s+[\w<>\[\]]+\s+\w+\s*\(',  # Method declaration
            r'Console\.(Write|WriteLine)',         # Console output
            r'\bvar\s+\w+\s*=',                   # Var keyword
            r'new\s+\w+\s*\(',                    # Object instantiation
            r'\bawait\s+',                         # Async/await
            r'\btask<',                            # Task object
            r'\bdynamic\b',                        # Dynamic type
            r'\bstring\b',                         # String type
            r'`\'\{0\}\'`'                         # String interpolation
        ]
        return any(re.search(pattern, code, re.IGNORECASE) for pattern in patterns)
        
    @staticmethod
    def detect_typescript(code: str) -> bool:
        """Detect if code is TypeScript."""
        patterns = [
            r':\s*[A-Za-z]+(?:<[^>]+>)?\s*(?:=|;|\)|\})',  # Type annotations
            r'interface\s+\w+\s*\{',               # Interface declaration
            r'class\s+\w+(?:\s+implements|\s+extends)?', # Class with implements or extends
            r'(private|public|protected)\s+\w+',    # Access modifiers
            r'\w+\s*<[^>]+>',                     # Generic types
            r'import\s+\{[^}]+\}\s+from',          # ES6 import
            r'export\s+(interface|class|type|const|let)', # Exports
            r'type\s+\w+\s*=',                     # Type aliases
            r'enum\s+\w+',                          # Enums
            r'@\w+(?:\([^)]*\))?'                  # Decorators
        ]
        
        # Check for TypeScript unique patterns AND JavaScript patterns (since TS is a superset of JS)
        ts_unique = any(re.search(pattern, code) for pattern in patterns)
        js_patterns = [
            r'function\s+\w+\s*\([^)]*\)',  # Function declaration
            r'const\s+\w+\s*=',             # Const declaration
            r'let\s+\w+\s*=',               # Let declaration
            r'var\s+\w+\s*=',               # Var declaration
            r'console\.(log|error|warn)'    # Console methods
        ]
        js_general = any(re.search(pattern, code) for pattern in js_patterns)
        
        return ts_unique and js_general
        
    @staticmethod
    def detect_r(code: str) -> bool:
        """Detect if code is R."""
        patterns = [
            r'<-\s*(?:function|\w+)',         # Assignment with <- 
            r'library\([\w\.]+\)',           # Library import
            r'(?:data|read)\.(?:frame|csv|table)', # Data frames
            r'\b(?:if|for|while)\s*\(',     # Control structures
            r'\$\w+',                       # Variable access with $
            r'\bNA\b|\bNULL\b|\bTRUE\b|\bFALSE\b', # R constants
            r'c\(.*?\)',                     # Vector creation with c()
            r'(?:plot|ggplot)\(',            # Plotting functions
            r'\s*#.*$',                      # R comments
            r'%>%',                          # Pipe operator
            r'\bfactor\(',                   # Factor function
            r'\bstr\(',                      # Structure function
            r'\bas\.\w+\(',                  # Type conversion functions
            r'\w+\s*<-\s*\w+\[.+?\]'        # Subsetting with brackets
        ]
        return any(re.search(pattern, code) for pattern in patterns)
        
    @staticmethod
    def detect_perl(code: str) -> bool:
        """Detect if code is Perl."""
        patterns = [
            r'\$\w+',                          # Scalar variables
            r'@\w+',                           # Array variables
            r'%\w+',                           # Hash variables
            r'use\s+[\w:]+\s*;',              # Module imports
            r'\bsub\s+\w+\s*\{',              # Subroutine definition
            r'\bmy\s+(?:\$|@|%)\w+',           # Variable declarations
            r'=~\s*(?:m|s|tr)',                # Regular expression operators
            r'print\s+(?:\$|@|%|")',           # Print statements
            r'(?:if|unless|while|for|foreach)\s*\(',  # Control structures
            r'\{.*?\}.*?\{.*?\}',              # Block structure typical in Perl
            r'->\w+',                          # Method calls
            r'\b(?:shift|pop|push|splice)',     # Array operations
            r';\s*$',                          # Statements ending with semicolon
            r'#.*$',                           # Comments
            r'\bdie\s+',                        # Die statements
            r'\bqw\s*\(',                       # qw() operator
            r'\$_',                             # Special $_ variable
            r'\bdefined\s+(?:\$|@|%)'           # Defined operator
        ]
        return any(re.search(pattern, code) for pattern in patterns)
        
    @staticmethod
    def detect_lua(code: str) -> bool:
        """Detect if code is Lua."""
        patterns = [
            r'\blocal\s+\w+',                    # Local variable declarations
            r'\bfunction\s+\w+(?:\w*\.\w+)*\s*\(', # Function definitions
            r'(?:end|then|do|else)\b',          # Lua keywords
            r'\brequire\s*\(["\w\.\']+\)',       # Module imports
            r'\breturn\s+.+?$',                  # Return statements
            r'\bnil\b',                          # Nil value
            r'\bfor\s+\w+\s*=\s*\d+\s*,\s*\d+', # Numeric for loops
            r'\bfor\s+\w+(?:\s*,\s*\w+)*\s+in\b', # Generic for loops
            r'\bif\s+.+?\s+then\b',              # If statements
            r'\belseif\s+.+?\s+then\b',           # Elseif statements
            r'\btable\.(\w+)\b',                 # Table library functions
            r'\bstring\.(\w+)\b',                # String library functions
            r'\bmath\.(\w+)\b',                  # Math library functions
            r'\bpairs\(\w+\)',                   # Pairs function
            r'\bipairs\(\w+\)',                  # Ipairs function
            r'\btostring\(',                     # Tostring function
            r'\btonumber\(',                     # Tonumber function
            r'\bprint\(',                        # Print function
            r'--.*$',                            # Comments
            r'\[\[.*?\]\]',                      # Multiline strings
            r'\{\s*[\w"\']+\s*=',                # Table initialization
            r'\w+\[\w+\]',                       # Table index access
            r'\w+\.\.\w+'                        # String concatenation
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    
    @staticmethod
    def detect_php(code: str) -> bool:
        """Detect if code is PHP."""
        patterns = [
            r'<\?php',                           # PHP opening tag
            r'\$\w+',                            # Variable with $ prefix
            r'function\s+\w+\s*\(',              # Function definition
            r'echo\s+[\$\w\'\"]+',                # Echo statement
            r'class\s+\w+(?:\s+extends|\s+implements)?', # Class definition
            r'(?:public|private|protected)\s+function', # Class methods
            r'(?:public|private|protected)\s+\$\w+', # Class properties
            r'namespace\s+[\w\\\\]+',              # Namespace declaration
            r'use\s+[\w\\\\]+',                    # Use statement
            r'=>',                               # Array key => value syntax
            r'array\s*\(',                       # Array creation
            r'\[\s*[\'\"]*\w+[\'\"]*\s*\]',        # Array access with []
            r'require(?:_once)?\s*\(',           # Require statements
            r'include(?:_once)?\s*\(',           # Include statements
            r'new\s+\w+',                        # Object instantiation
            r'->',                               # Object property/method access
            r'::',                               # Static property/method access
            r'<?=.*?(?:\?>|$)',                  # Short echo syntax
            r'if\s*\(.+?\)\s*\{',                # If statements
            r'foreach\s*\(\s*\$\w+',             # Foreach loops
            r';$'                                # Statement ending with semicolon
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    
    @staticmethod
    def detect_kotlin(code: str) -> bool:
        """Detect if code is Kotlin."""
        patterns = [
            r'fun\s+\w+\s*\(',                   # Function declaration
            r'val\s+\w+(?:\s*:\s*\w+)?',         # Val declaration
            r'var\s+\w+(?:\s*:\s*\w+)?',         # Var declaration
            r'class\s+\w+(?:\s*\((?:[^)]*)\))?', # Class declaration
            r'package\s+[\w\.]+',                # Package declaration
            r'import\s+[\w\.]+',                 # Import statement
            r'object\s+\w+',                     # Object declaration
            r'interface\s+\w+',                  # Interface declaration
            r'data\s+class',                     # Data class
            r'(?:override|open|abstract|final)\s+fun', # Modified functions
            r'(?:companion|sealed)\s+object',    # Special objects
            r'when\s*\(',                        # When expression
            r'(?:if|else|for|while)\s*\(',       # Control structures
            r'->',                               # Lambda syntax
            r'[\w\.\(\)]+\.\w+\{',               # Extension functions
            r'(?:List|Set|Map)<',                # Generic collections
            r'(?:private|public|internal|protected)', # Visibility modifiers
            r'lateinit\s+var',                   # Lateinit vars
            r'(?:suspend|inline)\s+fun',         # Special function modifiers
            r'@\w+(?:\([^)]*\))?'                # Annotations
        ]
        return any(re.search(pattern, code) for pattern in patterns)

    
    @staticmethod
    def detect_sql(code: str) -> bool:
        """Detect if code is SQL."""
        patterns = [
            r'SELECT\s+[\w\*,\s]+\s+FROM',       # SELECT statement
            r'INSERT\s+INTO\s+\w+',              # INSERT statement
            r'UPDATE\s+\w+\s+SET',               # UPDATE statement
            r'DELETE\s+FROM\s+\w+',              # DELETE statement
            r'CREATE\s+TABLE\s+\w+',             # CREATE TABLE statement
            r'ALTER\s+TABLE\s+\w+',              # ALTER TABLE statement
            r'DROP\s+TABLE\s+\w+',               # DROP TABLE statement
            r'TRUNCATE\s+TABLE\s+\w+',           # TRUNCATE TABLE statement
            r'JOIN\s+\w+\s+ON',                  # JOIN clause
            r'WHERE\s+\w+\s*(?:=|<|>|<=|>=|<>|!=|LIKE|IN)', # WHERE clause
            r'GROUP\s+BY\s+\w+',                 # GROUP BY clause
            r'ORDER\s+BY\s+\w+\s+(?:ASC|DESC)?', # ORDER BY clause
            r'HAVING\s+\w+',                     # HAVING clause
            r'CONSTRAINT\s+\w+',                 # CONSTRAINT declaration
            r'PRIMARY\s+KEY',                    # PRIMARY KEY constraint
            r'FOREIGN\s+KEY',                    # FOREIGN KEY constraint
            r'(?:VARCHAR|INT|INTEGER|FLOAT|DATE|DATETIME|BOOLEAN|TEXT|BLOB)', # Common data types
            r'(?:COUNT|SUM|AVG|MIN|MAX)\s*\(',   # Aggregate functions
            r'CASE\s+WHEN\s+.+?\s+THEN',         # CASE statement
            r'BEGIN\s+TRANSACTION',              # Transaction control
            r'COMMIT',                           # COMMIT statement
            r'ROLLBACK'                          # ROLLBACK statement
        ]
        return any(re.search(pattern, code, re.IGNORECASE) for pattern in patterns)


    def __init__(self):
        """Initialize language detector with detection functions."""
        self.detectors = {
            "Python": self.detect_python,
            "JavaScript": self.detect_javascript,
            "Java": self.detect_java,
            "C++": self.detect_cpp,
            "Julia": self.detect_julia,
            "Go": self.detect_go,
            "Ruby": self.detect_ruby,
            "Swift": self.detect_swift,
            "Rust": self.detect_rust,
            "C#": self.detect_csharp,
            "TypeScript": self.detect_typescript,
            "R": self.detect_r,
            "Perl": self.detect_perl,
            "Lua": self.detect_lua,
            "PHP": self.detect_php,
            "Kotlin": self.detect_kotlin,
            "SQL": self.detect_sql
        }


    def detect_language(self, code: str) -> str:
        """
        Detect the programming language of the given code.
        
        Args:
            code: Code snippet to analyze
            
        Returns:
            Detected language name or None if unknown
        """
        # Use a scoring system to prioritize more specific language patterns
        matches = {}
        
        # First pass: check which languages match
        for lang, detector in self.detectors.items():
            if detector(code):
                matches[lang] = 0
        
        if not matches:
            return None
            
        # If only one language matches, return it
        if len(matches) == 1:
            return list(matches.keys())[0]
            
        # Second pass: score the matches based on specific language features
        # These are language-specific unique patterns that are less likely to overlap
        unique_patterns = {
            "PHP": r'<\?php',
            "SQL": r'(?i)SELECT\s+[\w\*,\s]+\s+FROM',
            "Perl": r'\buse\s+[\w:]+\s*;|\bmy\s+(?:\$|@|%)',
            "Lua": r'\blocal\s+\w+|\bfunction\s+\w+(?:\w*\.\w+)*\s*\(',
            "Kotlin": r'\bfun\s+\w+\s*\(|\bval\s+\w+(?:\s*:\s*\w+)?',
            "Ruby": r'\bdef\s+\w+\s*(?:\([^)]*\))?\s*$|\bend\b',
            "TypeScript": r':\s*[A-Za-z]+(?:<[^>]+>)?\s*(?:=|;|\)|\})',
            "Swift": r'import\s+(?:Foundation|UIKit|SwiftUI)|@IBOutlet|@IBAction',
            "Rust": r'fn\s+\w+\s*\([^)]*\)\s*(?:->\s*[^{]+)?\s*\{|impl\s+\w+(?:\s+for\s+\w+)?',
            "C#": r'using\s+[\w.]+;|namespace\s+[\w.]+',
            "R": r'<-\s*(?:function|\w+)|library\([\w\.]+\)',
            "Python": r'def\s+\w+\s*\([^)]*\)\s*:|import\s+[\w\s,]+',
            "JavaScript": r'function\s+\w+\s*\([^)]*\)|const\s+\w+\s*=',
            "Java": r'public\s+class\s+\w+|public\s+static\s+void\s+main',
            "C++": r'#include\s*<[^>]+>|std::\w+',
            "Julia": r'function\s+\w+\s*\([^)]*\)\s*end|module\s+\w+',
            "Go": r'package\s+\w+|func\s+\w+\s*\('            
        }
        
        for lang in matches.keys():
            if lang in unique_patterns:
                pattern = unique_patterns[lang]
                if re.search(pattern, code):
                    matches[lang] += 2  # Give higher score for unique patterns
        
        # Additional scoring based on language-specific features
        if "<?php" in code:
            matches["PHP"] = matches.get("PHP", 0) + 5
        if re.search(r'SELECT\s+[\w\*,\s]+\s+FROM', code, re.IGNORECASE):
            matches["SQL"] = matches.get("SQL", 0) + 5
        if re.search(r'\bmy\s+\$\w+', code):
            matches["Perl"] = matches.get("Perl", 0) + 5
        if re.search(r'\blocal\s+\w+', code):
            matches["Lua"] = matches.get("Lua", 0) + 5
            
        # Kotlin-specific patterns with high scores
        kotlin_patterns = [
            (r'package\s+com\.', 8),  # Package declaration (common in Android)
            (r'import\s+android\.', 8),  # Android imports
            (r'import\s+kotlinx\.', 8),  # Kotlinx imports
            (r'fun\s+main\(\)', 7),  # Main function
            (r'class\s+\w+\s*:\s*\w+', 6),  # Class with inheritance
            (r'data\s+class', 8),  # Data class (very Kotlin specific)
            (r'companion\s+object', 8),  # Companion object (very Kotlin specific)
            (r'val\s+\w+\s*:\s*\w+', 5),  # Val with type
            (r'var\s+\w+\s*:\s*\w+', 5),  # Var with type
            (r'lateinit\s+var', 8),  # Lateinit (very Kotlin specific)
            (r'override\s+fun', 6),  # Override function
            (r'when\s*\(', 5),  # When expression
            (r'suspend\s+fun', 8),  # Coroutines (very Kotlin specific)
            (r'coroutineScope', 8),  # Coroutines scope
            (r'viewModel:', 6),  # ViewModel pattern
            (r'by\s+viewModels', 8),  # Delegation (very Kotlin specific)
            (r'by\s+lazy', 8),  # Lazy initialization (very Kotlin specific)
        ]
        
        for pattern, score in kotlin_patterns:
            if re.search(pattern, code):
                matches["Kotlin"] = matches.get("Kotlin", 0) + score
            
        # Return the language with the highest score
        if matches:
            return max(matches.items(), key=lambda x: x[1])[0]
        
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