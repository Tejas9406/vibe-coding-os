# 🚀 AI-Vibe Coding Agent: Quick Start Guide

Welcome! This is a simple cheat sheet to guide your AI agent through different workflows. 

For any task, start by telling your AI agent to read the base instructions (`AGENT.md`), choose the appropriate skill, and follow the template below.

---

## 🛠️ Choose Your Workflow

### 1. Starting a New Project from Scratch
Use this when you are building something completely new.
```markdown
Read AGENT.md
Read skills/00-core/project-orchestrator/SKILL.md

Problem Statement: [Describe your project]
Tech Stack: [e.g., React, Next.js, Node.js]

Instructions:
1. Classify project scope (Small/Medium/Large).
2. Complete Phase 1 (Understand) and Phase 2 (Design) first.
3. Show me the architecture & database schema before writing any code.
```

### 2. Updating an Existing Project
Use this to add a feature, fix a bug, or refactor code in an established project.
```markdown
Read AGENT.md
Read skills/03-development/token-optimizer/SKILL.md
Read skills/03-development/code-review/SKILL.md

Task: [e.g., Add Google OAuth, build user profile page]

Instructions:
1. Scan relevant files using `read_skeleton` (do not load whole files).
2. Locate exact code blocks to change using `read_symbol`.
3. Propose and apply changes, then run Code Reviewer to check them.
4. Use Git Commit Writer for a clean commit message.
```

### 3. Hackathons & Big Ideas (e.g., Smart India Hackathon - SIH)
Use this for building deep, robust, deployment-ready apps that align with government/sponsor goals.
```markdown
Read AGENT.md
Read skills/00-core/universal-project-builder/references/universal-master-blueprint.md

Problem Statement & Code: [e.g., SIH1423 - AI Crop Prediction]
Ministry/Organization: [e.g., Ministry of Agriculture]

Instructions:
1. Evaluate on Novelty, Industry Viability, and Policy/Government Inclusivity.
2. Complete design phases: Ground Reality, Stakeholder Map, Architecture, etc.
3. Show the Strategy Report first. Pass Quality Gates before writing code.
```

### 4. Pure Research (No Code)
Use this to analyze technologies, compare databases, or write reports without writing code.
```markdown
Read AGENT.md
Read skills/01-research/deep-research-team/SKILL.md

Research Topic: [e.g., pgvector vs Pinecone vs Milvus]
Goal: [e.g., Compare speed, latency, cost]
Mode: [Quick or Full]

Instructions:
1. Run the Deep Research Team workflow.
2. Cross-validate sources and output a structured markdown report. Do not write code.
```

### 5. Open Source Contributions
Use this when contributing to external codebases with strict guidelines.
```markdown
Read AGENT.md
Read skills/03-development/token-optimizer/SKILL.md
Read skills/03-development/code-review/SKILL.md

Issue/Feature: [Paste GitHub issue or details]

Instructions:
1. Check the project's contributing guidelines and conventions.
2. Map repository layout using `read_skeleton`.
3. Write a minimal, clean solution.
4. Run Code Reviewer to check for style issues or regressions.
```

### 6. Writing & Running Tests
Use this to write unit/integration tests or debug failing tests.
```markdown
Read AGENT.md
Read skills/03-development/token-optimizer/SKILL.md
Read skills/03-development/code-review/SKILL.md

Testing Goal: [e.g., Add Jest tests for all auth routes]

Instructions:
1. Find untested code.
2. Draft tests matching the existing test patterns.
3. Run tests using `exec_smart` to focus only on error/failure outputs.
```
