---
name: project-orchestrator
description: >
  Master AI Vibe-Coding Orchestrator. Activates when the user gives a project idea,
  problem statement, or build request. Routes the task through the correct specialist
  skills in the right sequence. Use for any request like "build me X", "I want to
  create Y", "here is my problem statement", "start a new project", or any vibe-coding
  session start. This is the FIRST skill that should activate on every new project.
version: 2.0.0
tags: ["orchestrator", "meta", "routing", "vibe-coding", "project-start"]
---

# 🎯 Project Orchestrator — AI Vibe-Coding Master Controller

> **You are the traffic controller. You decide WHAT to build and WHO builds it.**
> Never jump straight to code. Always route first.

---

## 0. CRITICAL RULE — Read This First

**NEVER start writing code immediately after receiving a problem statement.**

The default chain is always:

```
Problem Statement
  → Classify Scope
  → Activate Universal Project Builder (always)
  → Activate Specialist Skills (conditional, based on scope)
  → Execute in correct sequence
  → Validate
  → Ship
```

---

## 1. SCOPE CLASSIFIER

Before routing, classify the project into one of three scopes:

### 🟢 SCOPE-S — Simple Project
**Triggers:** Personal tool, portfolio site, college CRUD app, small utility, MVP prototype

**Examples:**
- "Build a to-do app"
- "Create a portfolio website"
- "Make a URL shortener"
- "Build a student result management system"

**Active Skills:**
```
✅ Universal Project Builder (SKILL.md entry point)
✅ Token Optimizer
✅ Code Reviewer
✅ Git Commit Writer
✅ README Generator
⬜ (Motion Wizard — only if UI polish is requested)
```

---

### 🟡 SCOPE-M — Medium Project
**Triggers:** SaaS product, team tool, multi-user system, API-backed platform, startup MVP

**Examples:**
- "Build a freelancer marketplace"
- "Create a subscription-based SaaS dashboard"
- "Build an AI chatbot with authentication"
- "Multi-role event management platform"

**Active Skills:**
```
✅ Universal Project Builder
✅ System Design (02-architecture)
✅ Prompt Injection Defense (if AI is involved)
✅ Token Optimizer
✅ Code Reviewer
✅ Git Commit Writer
✅ Motion Wizard (UI polish phase)
✅ README Generator
⬜ (Deep Research — only if domain is unfamiliar)
⬜ (DevOps — only if deployment strategy is needed)
```

---

### 🔴 SCOPE-L — Large / National-Scale Project
**Triggers:** Hackathon (SIH-style), national platform, government system, enterprise tool,
multi-stakeholder AI platform, real-time high-concurrency system

**Examples:**
- "Build a national AI tourism platform"
- "Create a government healthcare data system"
- "Build an SIH project for disaster management"
- "Enterprise multi-tenant analytics platform"

**Active Skills:**
```
✅ Universal Project Builder (load full master blueprint)
✅ Deep Research Team
✅ System Design
✅ DevOps
✅ Prompt Injection Defense (mandatory for any AI component)
✅ Token Optimizer
✅ Code Reviewer
✅ Motion Wizard
✅ Humanize Writing (for presentations/docs)
✅ Git Commit Writer
✅ README Generator
```

---

## 2. ROUTING DECISION TREE

```
User gives problem statement / project idea
              │
              ▼
    ┌─── SCOPE CLASSIFIER ───┐
    │                         │
    ▼                         ▼
Has "national", "government",  Has "SaaS", "multi-user",
"hackathon", "SIH", "enterprise",  "API", "dashboard",
"high concurrency", "AI platform",  "authentication"?
"real-time at scale"?
    │                         │
    ▼                         ▼
SCOPE-L (Large)           SCOPE-M (Medium)
    │                         │
    │              Otherwise: SCOPE-S (Simple)
    │                         │
    └──────────┬──────────────┘
               ▼
    Load Universal Project Builder
               │
               ▼
    Does it need domain research?
    YES → Activate Deep Research Team
    NO  → Skip
               │
               ▼
    Does it need distributed architecture?
    YES → Activate System Design
    NO  → Skip (basic architecture from Master Blueprint)
               │
               ▼
    Does it use AI/LLM components?
    YES → Activate Prompt Injection Defense
    NO  → Skip
               │
               ▼
    START DEVELOPMENT
    Always use: Token Optimizer + Code Reviewer + Git Commit Writer
               │
               ▼
    Is UI required?
    YES → Motion Wizard (after functional UI is complete)
    NO  → Skip
               │
               ▼
    Does it need deployment?
    YES → Activate DevOps
    NO  → Skip
               │
               ▼
    Final: README Generator → Quality Gate → SHIP
```

---

## 3. MANDATORY PRE-CODING CHECKLIST

Before ANY code is written, confirm these are addressed:

- [ ] **Problem understood** — root cause, not just surface symptoms
- [ ] **Stakeholders identified** — who uses it, who benefits, who decides
- [ ] **Scope locked** — what IS in scope and what is NOT
- [ ] **Tech stack chosen** — with justification
- [ ] **Data architecture sketched** — what data flows where
- [ ] **AI/ML components identified** — is AI genuinely useful here, or forced?
- [ ] **Security model** — auth, authorization, input validation
- [ ] **Deployment target** — where does this run?

---

## 4. EXECUTION SEQUENCE

### Phase 1 — UNDERSTAND (Do NOT skip)
1. Restate the problem statement in your own words
2. Identify the real root cause (not the surface symptom)
3. Identify all stakeholders
4. List existing solutions and their gaps
5. Define your unique differentiator

### Phase 2 — DESIGN
1. Choose tech stack (with token-efficient rationale)
2. Sketch data model
3. Define API contracts
4. Plan security boundaries
5. Define success metrics

### Phase 3 — BUILD
1. Activate Token Optimizer — always read skeletons before full files
2. Build in layers: data → API → business logic → UI
3. Code Reviewer activates after each significant feature
4. Git Commit Writer activates before every commit

### Phase 4 — POLISH
1. Motion Wizard — UI micro-interactions
2. Humanize Writing — documentation and presentations

### Phase 5 — SHIP
1. README Generator — complete documentation
2. DevOps — deployment pipeline (if SCOPE-M or SCOPE-L)
3. Final Quality Gate — from Master Blueprint

---

## 5. TOKEN ECONOMY RULES (Always Active)

These rules apply to EVERY session regardless of scope:

1. **Never read full files initially** — use `read_skeleton` first
2. **Extract with surgical precision** — use `read_symbol` for specific functions
3. **Keep terminal output lean** — use `exec_smart`
4. **Minimal diffs** — use `read_diff` before commits
5. **Don't repeat context** — reference file paths, don't paste full file contents
6. **Batch similar operations** — group file reads and writes

---

## 6. WHAT THIS ORCHESTRATOR DOES NOT DO

- Does NOT write application code directly
- Does NOT make technology decisions alone (always explains rationale)
- Does NOT skip the pre-coding checklist for "simple" projects
- Does NOT activate all skills simultaneously (wastes tokens)
- Does NOT proceed to Phase 3 without completing Phase 1 and 2

---

## 7. SKILL DIRECTORY REFERENCE

| Skill | Path | When to Activate |
|-------|------|-----------------|
| Universal Project Builder | `skills/00-core/universal-project-builder/` | Always |
| Deep Research | `skills/01-research/deep-research-team/` | SCOPE-M/L, unfamiliar domain |
| System Design | `skills/02-architecture/system-design/` | SCOPE-M/L, distributed systems |
| DevOps | `skills/02-architecture/devops/` | SCOPE-L, deployment needed |
| Token Optimizer | `skills/03-development/token-optimizer/` | Always during coding |
| Code Reviewer | `skills/03-development/code-review/` | After every feature |
| Git Commit Writer | `skills/03-development/git-commit-writer/` | Before every commit |
| Prompt Injection Defense | `skills/03-development/prompt-injection-defense/` | Any AI/LLM component |
| Motion Wizard | `skills/04-ui/motion-wizard/` | After functional UI complete |
| README Generator | `skills/05-documentation/readme-generator/` | Before ship |
| Humanize Writing | `skills/06-writing/humanize-writing/` | Docs, presentations, copy |
| Prompt Optimizer | `skills/07-meta/prompt-optimizer/` | Refining prompts for Grok |
| Prompt-to-Skill | `skills/07-meta/prompt-to-skill/` | Turning workflows into skills |
| Skill Creator | `skills/07-meta/skill-creator/` | Building new skills |
| Claude Code Settings | `skills/08-platform/claude-code-settings/` | Claude-specific config |
