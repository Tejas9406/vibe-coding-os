$ErrorActionPreference = "Stop"

Write-Host "Installing Token Optimizer MCP Server..." -ForegroundColor Cyan

$pythonExec = "python"
if (-Not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    if (Get-Command "python3" -ErrorAction SilentlyContinue) {
        $pythonExec = "python3"
    } else {
        Write-Host "Error: Python is not installed or not in PATH." -ForegroundColor Red
        exit 1
    }
}

Write-Host "Creating virtual environment..."
& $pythonExec -m venv venv

Write-Host "Installing dependencies..."
.\venv\Scripts\pip.exe install -e .

Write-Host ""
Write-Host "=================================================" -ForegroundColor Green
Write-Host "✅ Installation Complete!" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host ""

$venvPath = (Resolve-Path ".\venv\Scripts\python.exe").Path
# Escape backslashes for JSON
$venvPathJson = $venvPath -replace '\\', '\\\\'

Write-Host "Injecting configuration into Claude Desktop..." -ForegroundColor Cyan
& $venvPath .\inject_claude_config.py $venvPath

Write-Host "To use this MCP server, add the following to your MCP client config (e.g., mcp.json, Claude config):" -ForegroundColor Cyan
Write-Host @"
{
  "mcpServers": {
    "token-optimizer": {
      "command": "$venvPathJson",
      "args": [
        "-m",
        "token_optimizer.server"
      ]
    }
  }
}
"@

Write-Host ""
Write-Host "=================================================" -ForegroundColor Green
Write-Host "Cursor IDE Installation:" -ForegroundColor Cyan
Write-Host "1. Go to Cursor Settings > Features > MCP"
Write-Host "2. Click '+ Add New MCP Server'"
Write-Host "3. Name: token-optimizer"
Write-Host "4. Type: command"
Write-Host "5. Command: $venvPath"
Write-Host "6. Args: -m token_optimizer.server"
Write-Host "=================================================" -ForegroundColor Green
