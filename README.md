# 🚀 AI-Vibe Coding Agent: Quick Start Guide

Welcome! This is the master repository for universal coding agent skills. 

For any task, start by telling your AI agent to read the base instructions (`AGENT.md`), choose the appropriate skill, and follow the workflows below.

---

## 🛠️ Choose Your Workflow

### 1. Starting a New Project from Scratch
Use this when you are building something completely new.
```markdown
Read AGENT.md
Read skills/00-core/project-orchestrator/SKILL.md

Problem Statement: [Describe your project]
Tech Stack: [e.g., React, Next.js, FastAPI, Node.js]

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
1. Scan relevant files using skeletons or line-range reads (do not load whole files).
2. Locate exact code blocks to change.
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

### 4. UI Design & Modern Frontend
Use this to build beautiful interfaces with curated typography, harmonious color themes, and spring physics.
```markdown
Read AGENT.md
Read skills/04-ui/artifacts-builder/SKILL.md
Read skills/04-ui/theme-factory/SKILL.md
Read skills/04-ui/motion-wizard/SKILL.md

UI Goal: [e.g., Build a modern SaaS analytics dashboard with dark mode]
```

### 5. Automated E2E Testing (Playwright)
Use this to test web applications, check responsiveness, and prevent visual or API regressions.
```markdown
Read AGENT.md
Read skills/03-development/webapp-testing/SKILL.md

Testing Goal: [e.g., Test checkout flow and responsive design across desktop and mobile]
```

### 6. Document Generation (DOCX, PDF, PPTX, XLSX)
Use this when you need pitch decks, financial sheets, or formal reports.
```markdown
Read AGENT.md
Read skills/05-documentation/document-skills/[docx|pdf|pptx|xlsx]/SKILL.md

Document Goal: [e.g., Create a 10-slide presentation deck]
```

### 7. Pure Research (No Code)
Use this to analyze technologies, compare databases, or write reports without writing code.
```markdown
Read AGENT.md
Read skills/01-research/deep-research-team/SKILL.md

Research Topic: [e.g., pgvector vs Pinecone vs Milvus]
Goal: [e.g., Compare speed, latency, cost]
Mode: [Quick or Full]
```
