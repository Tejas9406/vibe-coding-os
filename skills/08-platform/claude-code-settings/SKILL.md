---
name: "Hooks & Settings for Claude Code"
description: "Master Claude Code's three-tier settings system (user / project / project-local) and the hook framework. Pick the right scope for the right rule, write hooks that are idempotent and don't fight the agent, and stop re-explaining preferences every session."
version: 1.0.0
author: Markus Isaksson
license: MIT
price: 0
tags: ["claude", "claude-code", "settings", "hooks", "configuration", "permissions", "workflow", "free"]
_agensi: "e81184ce-5a4f-4344-9ef4-e5ce6f1aee4c"
---

# Hooks & Settings for Claude Code

**Trigger Conditions:**
You want to make Claude Code's behavior durable — stop approving the same commands every session, run a formatter automatically after each edit, send a notification when a long task finishes, or block dangerous operations at the runtime layer instead of by convention.

**Do NOT use** for one-off task instructions (those go in the prompt) or for repo-level documentation about *what the code is* (that's CLAUDE.md, not settings).

## Why This Skill Exists

Claude Code has three durable surfaces that shape behavior: **settings** (rules and configuration), **CLAUDE.md** (project knowledge), and **memory** (facts about the user and project). New users mix these up — putting personal preferences in committed `.claude/settings.json`, putting build commands in memory instead of CLAUDE.md, putting code conventions in `settings.json` where they don't belong. The result is fragile configuration that doesn't survive collaborators, sessions, or reorganization.

This skill teaches the actual hierarchy, which surface owns which kind of decision, and the hook framework — Claude Code's most underused power tool.

## What You'll Gain

- A clean mental model of **what belongs in settings vs. CLAUDE.md vs. memory vs. the prompt**
- A repeatable rule for **which settings file (user / project / project-local)** any given setting should live in
- Working recipes for the most useful hooks (auto-format, block destructive ops, notify on completion, log Bash commands)
- Confidence that your committed `.claude/settings.json` is **safe to share with collaborators** — no personal credentials, no preferences that only apply to you

## When to Use This Skill

Use this skill when:
- You're tired of approving `npm test` 30 times per session
- You want Claude Code to auto-run a formatter after edits
- You want a notification on long-running tasks
- You're sharing a project with collaborators and want consistent agent behavior
- You want to block specific dangerous patterns (force-push, hook-skip, deploy-without-tag)
- You're setting up Claude Code on a new machine and want to mirror an existing config

**When You DON'T Need This Skill**
- One-off task instructions (just say them in the prompt)
- Project knowledge ("this repo uses Turborepo") — that's CLAUDE.md
- User facts ("I prefer terse responses") — that's memory, not settings
- MCP server setup — see the dedicated MCP connector skills

## Agent Operating Procedure

### Phase 1: Decide What Surface Owns the Decision

Before editing any config file, identify which surface should own the rule:

| Decision type | Belongs in | Example |
|---|---|---|
| "Auto-allow this Bash pattern" | **Settings** (permissions) | `npm test`, `git status`, `docker ps` |
| "Run X automatically on event Y" | **Settings** (hooks) | Format on PostToolUse, notify on Stop |
| "What this repo IS / how to build it" | **CLAUDE.md** | Build commands, sub-project layout, conventions |
| "Who the user is / their preferences" | **Memory** (user) | "Senior Go dev, new to React" |
| "How the user wants to collaborate" | **Memory** (feedback) | "Always run tests before claiming done" |
| "One-time instruction for THIS task" | **Prompt** | "Refactor this function to use streams" |

**Rule:** If you can't put it in one of these surfaces in a single sentence, you've got the wrong surface. The clearest signal of the right home is: "would this be useful to a fresh Claude session opening this repo tomorrow?"

### Phase 2: Choose the Right Settings File

Claude Code reads three settings files and merges them. Pick the right one:

| File | Scope | Committed? | Use for |
|---|---|---|---|
| `~/.claude/settings.json` | **User** (all your projects) | No | Personal preferences, theme, model defaults |
| `.claude/settings.json` | **Project**, committed | Yes | Rules every collaborator should follow — allowed Bash, project-wide hooks |
| `.claude/settings.local.json` | **Project, local only** | No (gitignore) | Per-user-per-project — paths only on your machine, personal hook overrides |

**Rule:** Never put credentials, API keys, or paths that contain your username in a committed `.claude/settings.json`. If you find yourself about to, it belongs in `settings.local.json` or an env var.

### Phase 3: Configure Permissions Correctly

The permissions block governs what Claude can do without prompting you. Default Claude Code prompts on every Bash command. After a few sessions you'll know which patterns are safe to auto-allow.

Minimal-good permissions for a TypeScript project:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run build:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(npx prisma:*)"
    ],
    "deny": [
      "Bash(git push --force:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

**Rule:** Allow narrow patterns, not broad ones. `Bash(npm:*)` allows any npm command including `npm publish` — too broad. `Bash(npm test:*)` is what you wanted.

### Phase 4: Write Effective Hooks

Hooks are shell commands the runtime fires on events. The four events worth knowing:

- **`PreToolUse`** — before a tool runs. Can block the tool by exiting non-zero.
- **`PostToolUse`** — after a tool ran successfully. Side-effects (notify, log, format).
- **`UserPromptSubmit`** — every time you submit a prompt. Useful for context injection.
- **`Stop`** — when Claude finishes a turn. Notifications, summaries.

Each hook is a shell command + a matcher pattern. The matcher controls when the hook fires.

**Recipe: auto-format TypeScript after every Edit/Write**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npx prettier --write \"$CLAUDE_FILE_PATH\" 2>/dev/null || true" }
        ]
      }
    ]
  }
}
```

**Recipe: desktop notification when a long turn completes (Windows)**

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "powershell -Command \"[reflection.assembly]::loadwithpartialname('System.Windows.Forms'); $notify = New-Object System.Windows.Forms.NotifyIcon; $notify.Icon = [System.Drawing.SystemIcons]::Information; $notify.Visible = $true; $notify.ShowBalloonTip(3000, 'Claude Code', 'Turn complete', 'Info')\"" }
        ]
      }
    ]
  }
}
```

**Recipe: log every Bash command to a file**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "echo \"[$(date -Iseconds)] $CLAUDE_TOOL_INPUT\" >> ~/.claude/bash-audit.log" }
        ]
      }
    ]
  }
}
```

**Rule:** Hooks must be **idempotent and fast.** A hook that takes 5 seconds slows every tool call by 5 seconds. A hook that has side-effects across runs (e.g., appends to a file without rotation) creates problems. Test each hook by running its command standalone before adding it.

### Phase 5: Activate & Verify

1. Save the settings file.
2. **Restart Claude Code.** Most settings (especially hooks and permissions) are read at session start.
3. Verify with `/config` inside the session — it shows the merged effective settings.
4. Test the hook by triggering its event. E.g., for `PostToolUse` on `Edit`, run a small edit and confirm the hook fired (formatter ran, log line appeared, notification surfaced).

If a hook silently does nothing, the most common causes: matcher doesn't match the tool name (matchers are case-sensitive: `Edit` not `edit`); shell variable expansion didn't happen because of quoting; the command exits non-zero on `PreToolUse` and blocks the tool (you may want `|| true` at the end).

## Common Pitfalls to Avoid

| Don't Do This | Do This Instead |
|---|---|
| Put `Bash(*:*)` in `allow` to stop the prompts | Allow narrow patterns; auto-allowing everything defeats the safety model |
| Commit `.claude/settings.json` with paths containing your username | Move it to `.claude/settings.local.json` (gitignored) |
| Write a `PreToolUse` hook with side effects | `PreToolUse` may run *before* the tool actually runs; side-effects belong in `PostToolUse` |
| Have a hook take >1s | Hooks fire on every matching event; a slow hook ruins responsiveness |
| Use settings for user preferences ("be terse") | That's a memory entry (feedback type), not a setting |
| Use settings for repo facts ("build with `pnpm dev`") | That's CLAUDE.md content, not a setting |
| Forget to restart after edits | Most settings need a restart to take effect; `/config` only shows current |
| Put MCP server entries in `settings.json` | MCP servers go in `~/.claude.json` (user) or `.mcp.json` (project) |
| Write a single mega-hook that does many things | One hook per concern; easier to debug and disable individually |

## Recommended Starting Prompt

```
I want to configure Claude Code so that [specific behavior]. Please apply the
Hooks & Settings for Claude Code skill: identify which surface should own this
(Phase 1), pick the right file scope (Phase 2), then write the config. Don't
forget to remind me which restarts and validations are needed.
```

## Works Well With

- **Plan Mode Mastery for Claude Code** (paid, $5) — Once you understand which decisions belong in durable config, Plan Mode Mastery teaches how to surface and approve the *non*-config decisions explicitly.
- **Managing Long Coding Sessions with Claude** (free) — Settings + CLAUDE.md + memory together are the three durable surfaces that survive session boundaries; this skill covers settings, that one covers the discipline of using all three.
- **Agensi MCP Connector with Claude** (paid, $7) — That skill applies this skill's principles to one specific configuration target (MCP server entries in `~/.claude.json`).

## Compatibility

Skills on Agensi follow the open SKILL.md standard and work with any compatible agent.

**Compatibility Note:** This skill is **specifically for Claude Code**. The three-tier settings hierarchy, the hook event names (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`), and the permissions allow/deny patterns are Claude Code's specific design. Grok Build, Cursor, Codex CLI, and Gemini CLI all have their own configuration models — different file paths, different event names, different semantics. No direct sibling skill exists for those agents.

---

## Permissions

**Permission Profile**: Configuration Read + Write

**Tools Used**

- **Read Files**: Yes — Inspect existing settings files before modifying.
- **Edit / Write**: Yes — Modify `~/.claude/settings.json`, `.claude/settings.json`, or `.claude/settings.local.json` as appropriate.
- **Bash (Terminal / Shell)**: Sometimes — Test hook commands standalone before adding them; verify hook execution via log files.
- **Glob / Grep**: Sometimes — Locate existing config files in unfamiliar projects.
- **WebFetch / WebSearch**: No
- **Network Access**: No

**Environment Variables**: None required by the skill itself; hooks may reference env vars.

**Allowed Hosts**: None

**File Scopes**:
- `~/.claude/settings.json` (user-scope)
- `.claude/settings.json` (project-scope, committed)
- `.claude/settings.local.json` (project-scope, local only)
- `~/.claude/bash-audit.log` and similar hook output paths (when recipes write logs)

**Notes**:
This skill is meta — it teaches the configuration discipline that other skills assume. Buyers of more advanced skills (Plan Mode Mastery, Memory System Architect) often discover after reading them that they need this foundation first. Free pricing matches its funnel role: this is the on-ramp to the paid ladder.
