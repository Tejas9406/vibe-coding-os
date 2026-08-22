# 📖 Universal AI-Vibe Agent & SIH Guide

> **Your Cheat Sheet for Vibe-Coding any task with maximum efficiency and minimal token usage.**

This file provides the exact prompts to feed your AI agent along with your task or problem statement. Always run these from the root directory of your workspace (or point the agent directly to these files).

---

## 1. How to Use on a Brand New Problem Statement (New Project)
Use this when you are starting a project from absolute scratch.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\00-core\project-orchestrator\SKILL.md

Problem Statement: [Paste your problem statement or project idea here]
Desired Tech Stack: [e.g., React + Node.js, Next.js + FastAPI, or "Suggest the most token-efficient stack"]

Instructions:
1. Classify this project scope (SCOPE-S / SCOPE-M / SCOPE-L) using the Project Orchestrator.
2. Complete Phase 1 (Understand) and Phase 2 (Design) first.
3. Stop and show me the proposed architecture & database schema before writing any code.
```

---

## 2. How to Use on an Existing Project (Adding Features / Updating Code)
Use this when you have an already established codebase and you want the agent to add a new page, fix a workflow, or update existing functions.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\token-optimizer\SKILL.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\code-review\SKILL.md

Task: [e.g., Add Google OAuth to the login page / Add a user profile page / Refactor the payment processing module]

Instructions:
1. Use D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\token-optimizer\SKILL.md to map out the relevant files using `read_skeleton` first. Do not load entire files.
2. Locate the precise code blocks to change using `read_symbol`.
3. Propose changes. Once approved, apply the changes and invoke the Code Reviewer to check the modification.
4. Use the Git Commit Writer to generate a clean conventional commit message.
```

---

## 3. How to Use for SIH & Hackathons (National-Scale Projects)
Use this to build robust, deployment-ready projects that impress hackathon judges, government bodies, and industry sponsors.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\00-core\universal-project-builder\references\universal-master-blueprint.md

SIH Problem Statement Code & Title: [e.g., SIH1423 - AI-Based Crop Yield Prediction]
Ministry/Organization: [e.g., Ministry of Agriculture]

Instructions:
1. Apply the 3-Tier Evaluation Matrix: Novelty/Tech Depth, Sponsor/Industry Viability, and Government Inclusivity/Policy Analytics.
2. Complete the comprehensive project lifecycle: Ground Reality → Root Cause → Stakeholder Map → Existing Solutions Audit → Unique Opportunity → Data & System Architecture Design.
3. Output the Complete Strategy Report first. Do not write code until the architecture design passes the Universal Quality Gates.
```

---

## 4. How to Use for Pure Research (No Code Writing)
Use this when you want to explore a topic, gather data, write reports, or analyze technologies without actually creating code files.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\01-research\deep-research-team\SKILL.md

Research Topic: [e.g., Comparative analysis of vector databases (pgvector vs Pinecone vs Milvus) for production RAG systems]
Research Goal: [e.g., Evaluate latency, indexing speed, host pricing, and ease of scaling]
Mode: [Quick (for swift analysis) or Full (for a multi-phase deep dive report)]

Instructions:
1. Run the Deep Research Team workflow using the PM and parallel research agents.
2. Collect evidence and cross-validate sources.
3. Output a structured, citation-rich markdown report outlining findings, comparisons, and final recommendations. Do not write project code.
```

---

## 5. How to Use for Open Source Contributions (Fixing Bugs / Adding Features)
Use this when contributing to an external repository where you must strictly adhere to the existing codebase structure, avoid regressions, and follow strict review guidelines.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\token-optimizer\SKILL.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\code-review\SKILL.md

GitHub Issue / Contribution Request: [Paste GitHub issue details or feature request description here]

Instructions:
1. Check the project's contributing guidelines (e.g., CONTRIBUTING.md) and coding conventions.
2. Map the existing repository architecture using `read_skeleton` first.
3. Draft a minimal, non-breaking solution targeting only the necessary files.
4. Pass the changes through the Code Reviewer, checking specifically for regressions and styling mismatches.
5. Create a detailed commit message with conventional commits and list testing steps.
```

---

## 6. How to Use for Testing Purposes
Use this when you want to write unit tests, integration tests, end-to-end tests, or run test suites to ensure codebase reliability.

```markdown
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\AGENT.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\token-optimizer\SKILL.md
Read D:\Projects\SKILL FILES\AI-Vibe-Coding-Agent\skills\03-development\code-review\SKILL.md

Testing Goal: [e.g., Write Jest unit tests for all auth routes / Add Cypress integration tests for user registration flow]

Instructions:
1. Scan current routes/files to identify untested files.
2. Draft tests using the appropriate framework (Jest, PyTest, Playwright, Cypress, etc.) matching current code conventions.
3. Execute the tests using `exec_smart` from the token optimizer to truncate long logs and focus only on failures.
4. Keep patching tests/code until all tests pass successfully.
```
