---
name: token-optimizer
description: Drastically reduces token usage and context bloat by reading structural skeletons, slicing symbols, and intelligently truncating logs and git diffs. Supports both dedicated MCP server tools and native agent tools.
tags: ["token-optimization", "performance", "ast", "context-management", "efficiency"]
version: 2.0.0
---

# ⚡ Token Optimizer Skill

This skill minimizes context window token usage during active development, preventing memory overflow, lowering latency, and drastically cutting API costs.

---

## 🛠️ Execution Protocol

### Mode A: When Token Optimizer MCP Tools Are Available
If the environment provides the `token-optimizer-mcp` tools, ALWAYS use them:
1. **Explore with Skeletons**: Use `read_skeleton` first to inspect imports, class signatures, and function headers without pulling in heavy method bodies or docstrings.
2. **Surgical Symbol Extraction**: When editing or reviewing a specific function or class, use `read_symbol` to pull *only* that target block into context.
3. **Truncate Terminal Noise**: When running tests or linters, execute via `exec_smart`. It strips passing tests and truncates error traces to the relevant 50 lines.
4. **Minimal Diffs**: Use `read_diff` before committing to inspect precise modified lines instead of re-reading entire files.

---

### Mode B: Native Agent Fallback (When MCP Server is Not Configured)
If the above MCP tools are not registered in your active toolset, follow these universal native agent best practices:
1. **Never load large files completely into context**:
   - Use `grep_search` / ripgrep to locate specific lines and symbols first.
   - Use line-range slice reading (e.g. `view_file` with `StartLine` and `EndLine` parameters) to inspect only the 50–100 lines you are modifying.
2. **Limit Terminal Output**:
   - Pipe large outputs or test results to tools that only display failures (e.g., `npm test -- --bail`, `pytest -q --tb=short`, or piping through `head -n 50`).
3. **Use Git Diffs for Verification**:
   - Inspect changes using `git diff -U2` or `git status --short` instead of re-reading all modified files from scratch.
4. **Targeted Edits**:
   - Use targeted find-and-replace tools (`replace_file_content`) instead of full file rewrites.
