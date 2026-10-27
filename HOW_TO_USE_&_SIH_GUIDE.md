# 📖 Universal AI-Vibe Agent & SIH Guide

> **Your Cheat Sheet for Vibe-Coding any task with maximum efficiency, minimal token usage, and production quality.**

This file provides the exact prompts to feed your AI agent along with your task or problem statement. Run these from your project directory (or adjust paths if referencing from a central skills folder like `D:/SKILLS`).

---

## 0. Universal Initial Agent Kickoff Prompt (One-Shot Recon & Setup)
Use this prompt as your opening command for **any** repository (new or existing) to instruct the AI agent to ingest the skills and prepare for production execution:

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

## 1. How to Use on a Brand New Problem Statement (New Project)
Use this when you are starting a project from absolute scratch.

```markdown
Read AGENT.md
Read skills/00-core/project-orchestrator/SKILL.md

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
Read AGENT.md
Read skills/03-development/token-optimizer/SKILL.md
Read skills/03-development/code-review/SKILL.md

Task: [e.g., Add Google OAuth to the login page / Add a user profile page / Refactor the payment processing module]

Instructions:
1. Use token-optimizer rules to inspect relevant files using line-range slices or skeletons first. Do not load entire files.
2. Locate the precise code blocks to change.
3. Propose changes. Once approved, apply the changes and invoke the Code Reviewer to check the modification.
4. Use the Git Commit Writer to generate a clean conventional commit message.
```

---

## 3. How to Use for SIH & Hackathons (National-Scale Projects)
Use this to build robust, deployment-ready projects that impress hackathon judges, government bodies, and industry sponsors.

```markdown
Read AGENT.md
Read skills/00-core/universal-project-builder/references/universal-master-blueprint.md

SIH Problem Statement Code & Title: [e.g., SIH1423 - AI-Based Crop Yield Prediction]
Ministry/Organization: [e.g., Ministry of Agriculture]

Instructions:
1. Apply the 3-Tier Evaluation Matrix: Novelty/Tech Depth, Sponsor/Industry Viability, and Government Inclusivity/Policy Analytics.
2. Complete the comprehensive project lifecycle: Ground Reality → Root Cause → Stakeholder Map → Existing Solutions Audit → Unique Opportunity → Data & System Architecture Design.
3. Output the Complete Strategy Report first. Do not write code until the architecture design passes the Universal Quality Gates.
```

---

## 4. How to Use for Frontend Polish & UI Design
Use this when building web applications, dashboards, or landing pages that need stunning aesthetics, cohesive typography/colors, and smooth animations.

```markdown
Read AGENT.md
Read skills/04-ui/artifacts-builder/SKILL.md
Read skills/04-ui/theme-factory/SKILL.md
Read skills/04-ui/motion-wizard/SKILL.md

UI Goal: [e.g., Build a modern SaaS analytics dashboard with dark mode and micro-interactions]

Instructions:
1. Select a cohesive color palette and typography pairing using Theme Factory.
2. Construct the layout and components using Artifacts Builder (React/Tailwind/shadcn).
3. Apply spring physics and micro-interactions using Motion Wizard (hardware-accelerated transforms, zero layout shifts).
```

---

## 5. How to Use for Web App E2E Testing
Use this to run automated browser testing and verify frontend workflows using Playwright.

```markdown
Read AGENT.md
Read skills/03-development/webapp-testing/SKILL.md

Testing Goal: [e.g., Verify user login flow, form submission, and responsive mobile layout]

Instructions:
1. Follow the webapp-testing decision tree.
2. Manage the dev server lifecycle using scripts/with_server.py if needed.
3. Write targeted Playwright test scripts, take screenshots of critical flows, and report any UI/API regressions.
```

---

## 6. How to Use for Pure Research (No Code Writing)
Use this when you want to explore a topic, gather data, write reports, or analyze technologies without actually creating code files.

```markdown
Read AGENT.md
Read skills/01-research/deep-research-team/SKILL.md

Research Topic: [e.g., Comparative analysis of vector databases (pgvector vs Pinecone vs Milvus) for production RAG systems]
Research Goal: [e.g., Evaluate latency, indexing speed, host pricing, and ease of scaling]
Mode: [Quick (for swift analysis) or Full (for a multi-phase deep dive report)]

Instructions:
1. Run the Deep Research Team workflow using the PM and parallel research agents.
2. Collect evidence and cross-validate sources.
3. Output a structured, citation-rich markdown report outlining findings, comparisons, and final recommendations. Do not write project code.
```

---

## 7. How to Use for Generating Professional Documents
Use this when you need Word (.docx), PDF, PowerPoint (.pptx), or Excel (.xlsx) deliverables for business presentations, government submissions, or client reports.

```markdown
Read AGENT.md
Read skills/05-documentation/document-skills/[docx|pdf|pptx|xlsx]/SKILL.md

Document Goal: [e.g., Create a 10-slide executive pitch deck for the SIH project / Generate an Excel financial forecast model]

Instructions:
1. Follow the specific document-skill formatting guidelines.
2. Use Python scripts to generate clean, professionally styled files with exact styling.
```

---

## 8. Centralized Reference Hint
If you keep your skills centralized in `D:/SKILLS`, prefix any `skills/...` path in the prompts with your global directory:
```markdown
Read D:/SKILLS/AGENT.md
Read D:/SKILLS/skills/00-core/project-orchestrator/SKILL.md
```
