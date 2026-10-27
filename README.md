# 🧠 Universal AI Agent Skills System (`SkillFiles_Universal`)

> **One problem statement in. A complete, production-ready project out.**  
> A universal, plug-and-play skill architecture designed for AI coding agents (Claude Code, Google Antigravity, Cursor, Windsurf, GitHub Copilot, Roo/Cline).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.txt)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![Platform: Universal](https://img.shields.io/badge/Platform-Universal%20Agentic-orange.svg)]()

---

## 🌟 What This Is

Most AI coding sessions fail because LLMs jump directly into writing shallow code, bloating the context window, hallucinating missing files, and creating unmaintainable architecture.

This repository provides a **battle-tested, multi-tier agent operating system**. Instead of acting as an isolated chatbot, the agent operates as a specialized engineering team:

1. **Traffic Controller & Project Orchestrator** — Classifies project scope (Small / Medium / Large / Hackathon) and selectively activates only required skills.
2. **System Architect & DevOps Engineer** — Formulates scalable system blueprints, CAP/BASE trade-offs, caching, and CI/CD pipelines before any code is generated.
3. **Execution & Quality Gates** — Enforces token-conscious file inspection, automated code review, conventional commits, and Playwright browser testing.
4. **UI & Creative Engine** — Replaces generic "AI-slop" designs with curated palettes, spring physics, Framer Motion transitions, and React/Tailwind/shadcn component systems.
5. **Production Deliverables** — Produces comprehensive READMEs, changelogs, and native Word (`.docx`), PDF, PowerPoint (`.pptx`), and Excel (`.xlsx`) files.

---

## ⚡ The ONE Golden Rule

> **Never start writing code before the Pre-Coding Checklist in the Universal Project Builder is complete.**

Every non-trivial project follows this chain:
```
Problem Statement 
   → Ground Reality Check 
   → Root Cause Analysis 
   → Stakeholder Mapping 
   → Architecture & Schema Design 
   → Layered Build 
   → Validation & E2E Testing 
   → Production Demo & Docs
```

---

## 🚀 How to Use Across Any Machine or Project

### ⚡ Universal Initial Agent Kickoff Prompt (Zero-Prompting Start)

Whenever you start an AI coding session in any agent (Claude Code, Google Antigravity, Cursor, Windsurf, Copilot, Roo/Cline) for an existing or new repository, **copy and paste this single initial prompt**:

```markdown
This is the repository we need to work on: [PASTE_REPO_URL_OR_LOCAL_PATH]
(e.g., https://github.com/Tejas9406/DastaavezAI.git or current workspace)

1. Fetch and scan the current codebase architecture, existing implementations, tech stack, and active dependencies.
2. Read the master operating instructions in AGENT.md and review the skills/ directory (which contains complete industry-standard production rules: orchestration, architecture, token-efficiency, UI polish, E2E testing, and quality gates).
3. Analyze what is currently working, what is half-implemented, and what architecture gaps exist.
4. Prepare the project to execute the next phase with 100% production readiness:
   - Zero errors / clean compilation
   - Fully connected pipelines & intact data flow
   - Optimal system design (load-handling, concurrency, caching, optimal time & space complexity)
   - Adherence to pre-coding quality gates before committing code changes.

Provide a concise reconnaissance summary of the current state, and stand by for my specific feature instructions.
```

---

### Method 1: Centralized Hub (Recommended — Zero Clutter)
Clone this repository **once** into a permanent location on your PC (e.g., `D:\SKILLS` on Windows, or `~/SKILLS` on macOS/Linux):

```bash
git clone https://github.com/Tejas9406/SkillFiles_Universal.git D:/SKILLS
```

Now, from **any project folder** in your terminal or IDE chat, tell your AI agent:
```markdown
Read D:/SKILLS/AGENT.md
Read D:/SKILLS/skills/00-core/project-orchestrator/SKILL.md

Problem Statement: [Paste your project idea or feature request here]
Desired Tech Stack: [e.g., Next.js + FastAPI + PostgreSQL, or "Suggest best stack"]
```

---

### Method 2: Drop-in Project Subfolder (`.agents/`)
If you want the skills directly contained within a specific repository for teammates or CI:

```bash
# Inside your project's root directory:
git clone --depth 1 https://github.com/Tejas9406/SkillFiles_Universal.git .agents
```

Then prompt your AI agent:
```markdown
Read .agents/AGENT.md
Read .agents/skills/00-core/project-orchestrator/SKILL.md

Problem Statement: [Paste your project idea here]
```

---

### Method 3: Global IDE Configuration
- **Claude Code**: Point your settings (`~/.claude/settings.json`) directly to the skills folder:
  ```json
  {
    "skills_path": "D:/SKILLS/skills"
  }
  ```
- **Antigravity IDE**: Place or link this repository inside your customizations root:
  - Global: `~/.gemini/config/skills/`
  - Workspace: `.agents/skills/`

---

## 📁 Master Skill Directory

```
skills/
├── 00-core/                      ← BRAIN (Always Active)
│   ├── project-orchestrator/     ← Routes tasks and classifies project scope (S/M/L)
│   └── universal-project-builder/← Full project lifecycle rules & quality gates
│       └── references/           (Universal Master Blueprint, Token Economy, 20+ Project Patterns)
│
├── 01-research/                  ← INTELLIGENCE
│   └── deep-research-team/       ← Multi-agent research team (PM, research, synthesis, audit)
│
├── 02-architecture/              ← SYSTEM STRUCTURE (Scope M/L)
│   ├── system-design/            ← High concurrency, CAP theorem, caching, message queues
│   └── devops/                   ← CI/CD pipelines, Docker, Kubernetes, GitOps, maturity matrices
│
├── 03-development/               ← BUILD, TESTING & SECURITY
│   ├── token-optimizer/          ← Context-efficient code reads (skeletons, slices, AST)
│   ├── code-review/              ← Senior engineer code review (bugs, security, performance)
│   ├── git-commit-writer/        ← Conventional Commits generator (`feat:`, `fix:`, etc.)
│   ├── webapp-testing/           ← Playwright automated browser E2E testing & server manager
│   ├── mcp-builder/              ← Model Context Protocol server creation (FastMCP / TS SDK)
│   └── prompt-injection-defense/ ← Security shield against LLM leaks & prompt injections
│
├── 04-ui/                        ← FRONTEND & POLISH
│   ├── artifacts-builder/        ← React 18 + Vite + Tailwind CSS + shadcn/ui component suite
│   ├── theme-factory/            ← 10 curated themes (color palettes & typography pairings)
│   ├── canvas-design/            ← Visual vector graphics and canvas art design
│   └── motion-wizard/            ← Framer Motion, spring physics, GPU transitions, zero-shift layouts
│
├── 05-documentation/             ← DELIVERABLES & SHIP
│   ├── readme-generator/         ← Automated documentation scanner & README builder
│   ├── changelog-generator/      ← Standardized KeepAChangelog releases
│   └── document-skills/          ← Programmatic generators for DOCX, PDF, PPTX, and XLSX
│
├── 06-writing/                   ← COMMUNICATION
│   └── humanize-writing/         ← Rewrites robotic AI prose into natural human text
│
├── 07-meta/                      ← SYSTEM UPGRADE
│   ├── prompt-optimizer/         ← Systematic prompt engineering for complex workflows
│   ├── prompt-to-skill/          ← Converts repeated prompts into reusable skills
│   └── skill-creator/            ← Builds and tests new skills
│
└── 08-platform/                  ← PLATFORM ADAPTERS
    └── claude-code-settings/     ← Claude Code hooks, permissions, and settings framework
```

---

## 🛠️ Ready-to-Use Workflow Prompts

### 1. New Project from Scratch
```markdown
Read AGENT.md
Read skills/00-core/project-orchestrator/SKILL.md

Problem Statement: [Describe your project]
Tech Stack: [e.g., React + Node.js, Next.js + FastAPI]

Instructions:
1. Classify project scope (Small / Medium / Large).
2. Complete Phase 1 (Understand) and Phase 2 (Design) first.
3. Show me the architecture & database schema before writing any code.
```

### 2. Updating an Existing Codebase
```markdown
Read AGENT.md
Read skills/03-development/token-optimizer/SKILL.md
Read skills/03-development/code-review/SKILL.md

Task: [e.g., Add Google OAuth authentication / Refactor payment module]

Instructions:
1. Scan relevant files using line-range slices or skeletons (never load whole files).
2. Propose targeted changes and apply them.
3. Run Code Reviewer to check for security, regressions, and style mismatches.
4. Generate a clean conventional commit message.
```

### 3. Smart India Hackathon (SIH) & High-Stakes Competitions
```markdown
Read AGENT.md
Read skills/00-core/universal-project-builder/references/universal-master-blueprint.md

SIH Problem Statement Code & Title: [e.g., SIH1423 - AI Crop Yield Prediction]
Ministry / Organization: [e.g., Ministry of Agriculture]

Instructions:
1. Apply the 3-Tier Evaluation Matrix (Novelty, Industry Viability, Policy/Government Inclusivity).
2. Execute the full lifecycle: Ground Reality → Root Cause → Stakeholder Map → Architecture.
3. Output the Complete Strategy Report first. Do not write code until design passes Quality Gates.
```

### 4. Modern UI & Frontend Polish
```markdown
Read AGENT.md
Read skills/04-ui/artifacts-builder/SKILL.md
Read skills/04-ui/theme-factory/SKILL.md
Read skills/04-ui/motion-wizard/SKILL.md

UI Goal: [e.g., Build a modern analytics dashboard with dark mode and micro-interactions]
```

### 5. Automated E2E Testing (Playwright)
```markdown
Read AGENT.md
Read skills/03-development/webapp-testing/SKILL.md

Testing Goal: [e.g., Verify checkout flow, auth states, and mobile responsive layout]
```

### 6. Professional Document Deliverables
```markdown
Read AGENT.md
Read skills/05-documentation/document-skills/[docx|pdf|pptx|xlsx]/SKILL.md

Document Goal: [e.g., Generate a 10-slide executive pitch deck for the product]
```

---

## 🔒 Safe & Self-Contained Design

- **No Root Collisions**: Contains no rogue `src/`, `tools/`, or `pyproject.toml` at the root that could overwrite your project files.
- **Universal Compatibility**: All skill definitions follow standardized YAML frontmatter compatible with all major agent frameworks.
- **Dual-Mode Execution**: Skills provide native agent tool fallbacks (`grep`, `view_file` line ranges, `git diff`) when specialized MCP servers are not running.

---

## 📄 License

This repository is distributed under the [MIT License](LICENSE.txt). Feel free to clone, customize, and integrate it into any commercial or personal workflow.
