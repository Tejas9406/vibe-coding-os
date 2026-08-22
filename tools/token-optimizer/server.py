from typing import Optional
from fastmcp import FastMCP
from .tools import extract_skeleton, extract_symbol, exec_smart as tools_exec_smart, read_diff as tools_read_diff

mcp = FastMCP("token-optimizer-mcp")

@mcp.tool()
def read_skeleton(file_path: str, language: Optional[str] = None) -> str:
    """Generates an AST-parsed structural outline of a source file (imports, class signatures, function headers, type definitions) with implementation bodies stripped to save tokens.
    
    Args:
        file_path: Path to the source file.
        language: Optional language (e.g. 'python', 'typescript'). Auto-detected if omitted.
    """
    return extract_skeleton(file_path, language)

@mcp.tool()
def read_symbol(file_path: str, symbol_name: str) -> str:
    """Extracts ONLY the specified function, class, or type definition block from a file without loading surrounding boilerplate into context.
    
    Args:
        file_path: Path to the source file.
        symbol_name: Name of the target function, class, interface, or variable definition.
    """
    return extract_symbol(file_path, symbol_name)

@mcp.tool()
def exec_smart(command: str, max_error_lines: int = 50) -> str:
    """Executes a shell command (test runner, compiler, linter) and automatically strips passing test output, returning ONLY failure stack traces, exit codes, and error lines.
    
    Args:
        command: The command to execute.
        max_error_lines: Maximum number of error stack trace lines to retain per failure. Default is 50.
    """
    return tools_exec_smart(command, max_error_lines)

@mcp.tool()
def read_diff(file_path: Optional[str] = None) -> str:
    """Returns a compact git patch/diff of uncommitted edits for a specific file or repository working tree instead of re-reading full files into context.
    
    Args:
        file_path: Optional path to a specific file. If omitted, returns diff summary across working tree.
    """
    return tools_read_diff(file_path)

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
