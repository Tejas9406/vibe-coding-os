---
name: token-optimizer
description: Drastically reduces token usage and context bloat by parsing ASTs to extract code skeletons and symbols, and intelligently truncating logs and git diffs.
_agensi: "da694fc6-258b-4391-aa5c-f14746e0bc10"
---

# Token Optimizer Skill

This skill equips you with the Token Optimizer MCP server, which is designed to drastically reduce context window token usage during active development, saving users up to 90% in API costs and preventing memory overflow during long sessions.

## Execution Rules

To minimize context window usage, lower latency, and reduce API costs, ALWAYS adhere to these execution rules:

1. **NEVER read full files initially.** When exploring a codebase, ALWAYS use `read_skeleton` first to map out the structure (classes, function signatures) without reading the heavy implementation bodies, docstrings, or comments.
2. **Extract with surgical precision.** When you need to edit or review a specific function or class, use `read_symbol` to pull *only* that specific block of code into your context.
3. **Keep terminal logs lean.** When running tests, compilers, or linters, ALWAYS use `exec_smart`. It will automatically strip passing outputs and truncate failing stack traces to the most critical lines so you don't flood your context window.
4. **Read minimal diffs.** When verifying changes before a commit, use `read_diff` to get a unified diff with only 1 line of context, rather than pulling the entire file back into memory.

By following these rules, you will act as a highly efficient, token-optimized agent!
