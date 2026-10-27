#!/bin/bash
set -e

echo "Installing Token Optimizer MCP Server..."

# Fallback to python3 if python is not available
PYTHON_CMD="python"
if ! command -v python &> /dev/null; then
    PYTHON_CMD="python3"
fi

if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "Error: Python is not installed or not in PATH."
    exit 1
fi

echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

echo "Installing dependencies..."
./venv/bin/pip install -e .

echo ""
echo "================================================="
echo "✅ Installation Complete!"
echo "================================================="
echo ""
echo "To use this MCP server, add the following to your MCP client config (e.g., mcp.json, Claude config):"

VENV_PATH="$(pwd)/venv/bin/python"

echo "Injecting configuration into Claude Desktop..."
$VENV_PATH inject_claude_config.py "$VENV_PATH"

cat << EOF
{
  "mcpServers": {
    "token-optimizer": {
      "command": "$VENV_PATH",
      "args": [
        "-m",
        "token_optimizer.server"
      ]
    }
  }
}
EOF

echo ""
echo "================================================="
echo "Cursor IDE Installation:"
echo "1. Go to Cursor Settings > Features > MCP"
echo "2. Click '+ Add New MCP Server'"
echo "3. Name: token-optimizer"
echo "4. Type: command"
echo "5. Command: $VENV_PATH"
echo "6. Args: -m token_optimizer.server"
echo "================================================="
