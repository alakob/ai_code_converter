"""Module for executing code in different programming languages."""

import contextlib
import io
import logging
import os
import re
import subprocess
import tempfile
from typing import Optional
from datetime import datetime
from src.ai_code_converter.utils.logger import setup_logger
from pathlib import Path

# Initialize logger for this module
logger = setup_logger(__name__)

class CodeExecutor:
    """Class for executing code in various programming languages."""
    
    def __init__(self):
        """Initialize the code executor."""
        logger.info("Initializing CodeExecutor")
        self.executors = {
            "Python": self.execute_python,
            "JavaScript": self.execute_javascript,
            "Java": self.execute_java,
            "C++": self.execute_cpp,
            "Julia": self.execute_julia,
            "Go": self.execute_go
        }

    def execute(self, code: str, language: str) -> tuple[str, Optional[bytes]]:
        """Execute code with detailed logging."""
        logger.info("="*50)
        logger.info(f"STARTING CODE EXECUTION: {language}")
        logger.info("="*50)
        logger.info(f"Code length: {len(code)} characters")
        
        if not code:
            logger.warning("No code provided for execution")
            return "No code to execute", None
        
        executor = self.executors.get(language)
        if not executor:
            logger.error(f"No executor found for language: {language}")
            return f"Execution not implemented for {language}", None
        
        try:
            logger.info(f"Executing {language} code")
            start_time = datetime.now()
            
            output, binary = executor(code)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.info(f"Execution completed in {execution_time:.2f} seconds")
            logger.info(f"Output length: {len(output)} characters")
            if binary:
                logger.info(f"Binary size: {len(binary)} bytes")
            logger.info("="*50)
            
            return f"{output}\nExecution completed in {execution_time:.2f} seconds", binary
            
        except Exception as e:
            logger.error(f"Error executing {language} code", exc_info=True)
            logger.info("="*50)
            return f"Error: {str(e)}", None

    def execute_python(self, code: str) -> tuple[str, Optional[bytes]]:
        """Execute Python code in a safe environment."""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            try:
                # Create a shared namespace for globals and locals
                namespace = {}
                
                # Execute the code with shared namespace
                exec(code, namespace, namespace)
                
                # Get any stored output
                execution_output = output.getvalue()
                
                # If there's a result variable, append it to output
                if '_result' in namespace:
                    execution_output += str(namespace['_result'])
                    
                return execution_output, None
            except Exception as e:
                logger.error(f"Python execution error: {str(e)}", exc_info=True)
                return f"Error: {str(e)}", None
            finally:
                output.close()

    def execute_javascript(self, code: str) -> tuple[str, Optional[bytes]]:
        """Execute JavaScript code using Node.js."""
        with tempfile.NamedTemporaryFile(suffix='.js', mode='w', delete=False) as f:
            f.write(code)
            js_file = f.name
            
        try:
            result = subprocess.run(
                ["node", js_file],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout, None
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}", None
        except Exception as e:
            return f"Error: {str(e)}", None
        finally:
            os.unlink(js_file)

    def execute_julia(self, code: str) -> tuple[str, Optional[bytes]]:
        """Execute Julia code."""
        with tempfile.NamedTemporaryFile(suffix='.jl', mode='w', delete=False) as f:
            f.write(code)
            jl_file = f.name
            
        try:
            result = subprocess.run(
                ["julia", jl_file],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout, None
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}", None
        except Exception as e:
            return f"Error: {str(e)}", None
        finally:
            os.unlink(jl_file)

    def execute_cpp(self, code: str) -> tuple[str, Optional[bytes]]:
        """Compile and execute C++ code."""
        with tempfile.NamedTemporaryFile(suffix='.cpp', mode='w', delete=False) as f:
            f.write(code)
            cpp_file = f.name
            
        try:
            # Compile
            exe_file = cpp_file[:-4]  # Remove .cpp
            if os.name == 'nt':  # Windows
                exe_file += '.exe'
                
            compile_result = subprocess.run(
                ["g++", cpp_file, "-o", exe_file],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Execute
            run_result = subprocess.run(
                [exe_file],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Read the compiled binary
            with open(exe_file, 'rb') as f:
                compiled_binary = f.read()
            
            return run_result.stdout, compiled_binary
            
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}", None
        except Exception as e:
            return f"Error: {str(e)}", None
        finally:
            os.unlink(cpp_file)
            if os.path.exists(exe_file):
                os.unlink(exe_file)

    def execute_java(self, code: str) -> tuple[str, Optional[bytes]]:
        """Compile and execute Java code."""
        logger.info("Starting Java code execution")
        
        # Create a temporary directory with proper permissions
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                # Extract class name
                class_match = re.search(r'public\s+class\s+(\w+)', code)
                if not class_match:
                    logger.error("Could not find public class name in Java code")
                    return "Error: Could not find public class name", None
                    
                class_name = class_match.group(1)
                temp_path = Path(temp_dir)
                java_file = temp_path / f"{class_name}.java"
                class_file = temp_path / f"{class_name}.class"
                
                # Write code to file
                java_file.write_text(code)
                logger.info(f"Wrote Java source to {java_file}")
                
                # Compile
                logger.info("Compiling Java code")
                compile_result = subprocess.run(
                    ["javac", str(java_file)],
                    capture_output=True,
                    text=True,
                    check=True,
                    cwd=temp_dir  # Set working directory to temp_dir
                )
                logger.info("Java compilation successful")
                
                # Verify class file exists
                if not class_file.exists():
                    logger.error(f"Class file {class_file} not found after compilation")
                    return "Error: Compilation failed to produce class file", None
                
                # Read compiled bytecode
                compiled_binary = class_file.read_bytes()
                logger.info(f"Read compiled binary, size: {len(compiled_binary)} bytes")
                
                # Execute
                logger.info("Executing Java code")
                run_result = subprocess.run(
                    ["java", class_name],
                    capture_output=True,
                    text=True,
                    check=True,
                    cwd=temp_dir  # Set working directory to temp_dir
                )
                logger.info("Java execution successful")
                
                # Return both output and compiled binary
                return run_result.stdout, compiled_binary
                
            except subprocess.CalledProcessError as e:
                logger.error(f"Java compilation/execution error: {e.stderr}")
                return f"Error: {e.stderr}", None
            except Exception as e:
                logger.error(f"Unexpected error in Java execution: {str(e)}", exc_info=True)
                return f"Error: {str(e)}", None

    def execute_go(self, code: str) -> tuple[str, Optional[bytes]]:
        """Execute Go code."""
        with tempfile.NamedTemporaryFile(suffix='.go', mode='w', delete=False) as f:
            f.write(code)
            go_file = f.name
            
        try:
            # Compile first
            exe_file = go_file[:-3]  # Remove .go
            if os.name == 'nt':
                exe_file += '.exe'
            
            compile_result = subprocess.run(
                ["go", "build", "-o", exe_file, go_file],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Read compiled binary
            with open(exe_file, 'rb') as f:
                compiled_binary = f.read()
            
            # Execute
            run_result = subprocess.run(
                [exe_file],
                capture_output=True,
                text=True,
                check=True
            )
            return run_result.stdout, compiled_binary
            
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}", None
        except Exception as e:
            return f"Error: {str(e)}", None
        finally:
            os.unlink(go_file)
            if os.path.exists(exe_file):
                os.unlink(exe_file) 