import os
import subprocess
from pathlib import Path
from typing import Optional

def guess_language(file_path: str) -> str:
    """Guess the programming language of a file based on its extension."""
    ext = Path(file_path).suffix.lower()
    mapping = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.rs': 'rust',
        '.go': 'go',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.cc': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp'
    }
    return mapping.get(ext, 'python')

def get_ast_parser(language: str):
    """Dynamically load and return a tree-sitter parser for the given language."""
    try:
        from tree_sitter_languages import get_parser
        return get_parser(language)
    except ImportError:
        raise RuntimeError("tree-sitter-languages is not installed.")

def get_body_node(node):
    """Find and return the main body block of a function or class node."""
    body = node.child_by_field_name('body')
    if body:
        return body
    
    block_types = ['block', 'statement_block', 'compound_statement']
    for child in node.children:
        if child.type in block_types:
            return child
    return None

def extract_skeleton(file_path: str, language: Optional[str] = None) -> str:
    """
    Reads a file and returns its structural skeleton by stripping out function/method implementation bodies, 
    comments, and docstrings using AST parsing.
    """
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found."
    
    if not language:
        language = guess_language(file_path)
    
    with open(file_path, 'rb') as f:
        source_code = f.read()
        
    try:
        parser = get_ast_parser(language)
    except Exception as e:
        return f"Error loading parser for {language}: {e}"
        
    tree = parser.parse(source_code)
    
    function_node_types = {
        'function_definition', 'function_declaration', 'method_definition', 
        'arrow_function', 'function_item', 'method_declaration', 'constructor_declaration'
    }
    
    nodes_to_strip = []
    
    def walk(node):
        if node.type in function_node_types:
            body_node = get_body_node(node)
            if body_node:
                nodes_to_strip.append(body_node)
        # Ultra Token Savings: Strip comments and docstrings
        elif node.type in ('comment', 'line_comment', 'block_comment'):
            nodes_to_strip.append(node)
        elif language == 'python' and node.type == 'expression_statement':
            if len(node.children) == 1 and node.children[0].type == 'string':
                nodes_to_strip.append(node)
                
        for child in node.children:
            walk(child)
            
    walk(tree.root_node)
    
    # Sort nodes by start_byte
    nodes_to_strip.sort(key=lambda n: n.start_byte)
    
    result = bytearray()
    last_idx = 0
    
    for node in nodes_to_strip:
        # Don't overlap
        if node.start_byte < last_idx:
            continue
            
        result.extend(source_code[last_idx:node.start_byte])
        
        if language == 'python':
            # Preserve indentation
            # Find the column of the block
            indent = " " * node.start_point[1]
            result.extend(f"\n{indent}...".encode('utf-8'))
        else:
            result.extend(b"{ ... }")
            
        last_idx = node.end_byte
        
    result.extend(source_code[last_idx:])
    
    return result.decode('utf-8', errors='replace')

def get_symbol_name(node) -> Optional[str]:
    """Attempt to extract the name identifier of a given AST definition node."""
    name_node = node.child_by_field_name('name')
    if name_node:
        return name_node.text.decode('utf-8', errors='ignore')
        
    for child in node.children:
        if child.type in ['identifier', 'property_identifier', 'type_identifier']:
            return child.text.decode('utf-8', errors='ignore')
    return None

def extract_symbol(file_path: str, symbol_name: str, language: Optional[str] = None) -> str:
    """
    Searches the AST of a file for a specific function, class, or variable definition and returns 
    only that specific block of code.
    """
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found."
        
    if not language:
        language = guess_language(file_path)
        
    with open(file_path, 'rb') as f:
        source_code = f.read()
        
    try:
        parser = get_ast_parser(language)
    except Exception as e:
        return f"Error loading parser for {language}: {e}"
        
    tree = parser.parse(source_code)
    
    target_nodes = []
    
    # We look for nodes that define something
    def walk(node):
        # typically definitions have a name child
        name = get_symbol_name(node)
        if name == symbol_name:
            target_nodes.append(node)
            
        for child in node.children:
            walk(child)
            
    walk(tree.root_node)
    
    if not target_nodes:
        return f"Error: Symbol '{symbol_name}' not found in {file_path}."
        
    # Return the first matching node that is a statement/declaration (usually higher in the tree)
    # We can just sort by size descending to get the largest enclosing definition
    target_nodes.sort(key=lambda n: n.end_byte - n.start_byte, reverse=True)
    best_node = target_nodes[0]
    
    return source_code[best_node.start_byte:best_node.end_byte].decode('utf-8', errors='replace')

def exec_smart(command: str, max_error_lines: int = 30) -> str:
    """
    Executes a shell command. If successful, strips the output to save tokens. 
    If it fails, returns only the final `max_error_lines` of the stack trace.
    """
    try:
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, # Merge stderr into stdout
            text=True
        )
        
        if process.returncode == 0:
            return f"Command `{command}` executed successfully.\nOutput stripped to save tokens."
            
        lines = process.stdout.splitlines()
        error_tail = lines[-max_error_lines:] if len(lines) > max_error_lines else lines
        
        out = f"Command `{command}` failed with exit code {process.returncode}.\n"
        out += f"--- Last {len(error_tail)} lines of output ---\n"
        out += "\n".join(error_tail)
        return out
        
    except Exception as e:
        return f"Failed to execute command: {e}"

def read_diff(file_path: Optional[str] = None) -> str:
    """
    Returns a unified git diff (with 1 line of context) for uncommitted changes.
    Can be restricted to a specific file.
    """
    try:
        # Check if we are in a git repo
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, capture_output=True)
        
        cmd = ["git", "diff", "-U1", "HEAD"]
        if file_path:
            cmd.extend(["--", file_path])
            
        process = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        if not process.stdout.strip():
            return "No uncommitted changes."
            
        return process.stdout
    except subprocess.CalledProcessError:
        return "Error: Not a git repository or git command failed."
    except FileNotFoundError:
        return "Error: git is not installed or not in PATH."
