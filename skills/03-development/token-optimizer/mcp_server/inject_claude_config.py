import os
import sys
import json
import platform
from pathlib import Path

def get_claude_config_path() -> Path:
    system = platform.system()
    if system == "Windows":
        return Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json"
    elif system == "Darwin":
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    else:
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"

def inject_config(venv_python_path: str):
    config_path = get_claude_config_path()
    
    # Ensure the directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    config = {}
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    config = json.loads(content)
        except Exception as e:
            print(f"Warning: Could not read existing config at {config_path}: {e}")
            return

    if "mcpServers" not in config:
        config["mcpServers"] = {}
        
    # Inject our server
    config["mcpServers"]["token-optimizer"] = {
        "command": venv_python_path,
        "args": ["-m", "token_optimizer.server"]
    }
    
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        print(f"[SUCCESS] Successfully injected token-optimizer into Claude Desktop config!")
        print(f"   ({config_path})")
    except Exception as e:
        print(f"Error: Could not write to config file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inject_claude_config.py <path_to_venv_python>")
        sys.exit(1)
        
    inject_config(sys.argv[1])
