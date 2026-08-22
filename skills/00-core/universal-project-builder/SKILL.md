---
name: universal-project-builder
description: >
  Universal AI Vibe-Coding project builder. The complete lifecycle skill for building
  serious, production-worthy projects. Activates after the Project Orchestrator classifies
  scope. Contains the universal rules, mandatory lifecycle, and links to the full master
  blueprint. Use for any non-trivial project that goes beyond a single-file script.
  Always pairs with the Project Orchestrator.
version: 2.0.0
tags: ["universal", "project-builder", "vibe-coding", "lifecycle", "hackathon", "SIH"]
---

# 🏗️ Universal Project Builder

> *"Build deep, not wide. Build AI-native, not AI-wrapped. Build for performance, not just features."*

---

## 0. CRITICAL — Full Master Blueprint

**For national-scale, enterprise, or hackathon projects**, read the full master blueprint:

📖 **`references/universal-master-blueprint.md`** — 2,462 lines of complete project lifecycle rules

**For smaller projects (SCOPE-S)**, use only the sections below.

---

## 1. UNIVERSAL PROJECT LIFECYCLE

This chain MUST be followed regardless of project scope:

```
Problem Statement
  │
  ▼
1. GROUND REALITY CHECK
   → What is actually happening in the real world?
   → Primary data: surveys, reports, government data
   → Secondary data: existing research, competitors
  │
  ▼
2. ROOT CAUSE ANALYSIS
   → Why does this problem exist?
   → What is the actual pain, not the symptom?
   → Who suffers most and how?
  │
  ▼
3. STAKEHOLDER MAP
   → Primary users (who uses it daily)
   → Secondary stakeholders (who benefits indirectly)
   → Decision makers (who approves / pays for it)
   → Adversarial actors (who might misuse it)
  │
  ▼
4. EXISTING SOLUTIONS AUDIT
   → What solutions already exist?
   → Why have they failed or fallen short?
   → What gaps remain unaddressed?
  │
  ▼
5. OPPORTUNITY DEFINITION
   → What unique position can this solution occupy?
   → What differentiates this from everything else?
  │
  ▼
6. SOLUTION DESIGN
   → Architecture decision (Monolith / Microservices / Serverless)
   → Data model and flow
   → AI/ML integration (only where genuinely useful)
   → Security model
   → Performance targets
   → UX principles
  │
  ▼
7. BUILD (in layers)
   → Data layer first
   → API / business logic second
   → UI / frontend third
   → AI/ML components fourth (integrated, not bolted on)
  │
  ▼
8. VALIDATE
   → Unit tests for critical paths
   → Integration tests for API contracts
   → User-acceptance criteria
   → Performance benchmarks
  │
  ▼
9. ADOPTION DESIGN
   → How will users actually find and adopt this?
   → What is the onboarding experience?
   → What metrics define success?
  │
  ▼
10. SHIP & DEMO
    → Live, crash-proof demo
    → Clear presentation narrative
    → README that a new developer can follow
```

---

## 2. TECHNOLOGY SELECTION RULES

### Choose based on actual requirements, not trends:

| Need | Default Choice | Upgrade When |
|------|---------------|-------------|
| Web Frontend | React + TypeScript | Next.js when SSR/SEO needed |
| Backend API | Node.js / FastAPI | Go/Rust for high-concurrency |
| Database (relational) | PostgreSQL | MySQL for read-heavy legacy |
| Database (document) | MongoDB | Only when schema is genuinely flexible |
| Cache | Redis | Memcached for pure caching |
| Queue | Redis BullMQ | RabbitMQ / Kafka for high throughput |
| AI/ML | Python (scikit-learn, HuggingFace) | PyTorch for custom models |
| LLM Integration | OpenAI API / local Ollama | Fine-tune only when necessary |
| Mobile | React Native | Flutter when native performance critical |
| DevOps | Docker + GitHub Actions | Kubernetes when >3 services |
| Auth | NextAuth / Passport.js | Custom only for specific compliance |

---

## 3. UNIVERSAL QUALITY GATES

Before calling any feature "done":

### Code Quality
- [ ] No hardcoded secrets or API keys (use environment variables)
- [ ] Error handling on every external call (API, DB, file I/O)
- [ ] Input validation on every user-facing endpoint
- [ ] No console.log / print debugging left in production code
- [ ] Functions under 50 lines (split if longer)
- [ ] Types defined for all data structures (TypeScript / Python type hints)

### Security (Non-Negotiable)
- [ ] Authentication on all protected routes
- [ ] Authorization checks (not just authn — users can only access their own data)
- [ ] SQL/NoSQL injection prevention
- [ ] XSS prevention
- [ ] Rate limiting on all public endpoints
- [ ] CORS configured properly (not `*` in production)
- [ ] Secrets in `.env` files, `.env` in `.gitignore`

### Performance
- [ ] Database queries use indexes on filtered/sorted fields
- [ ] No N+1 query problems
- [ ] Images optimized and lazy-loaded
- [ ] API responses paginated for lists > 100 items
- [ ] Caching implemented for expensive repeated queries

### Accessibility
- [ ] Semantic HTML (`<nav>`, `<main>`, `<article>`, etc.)
- [ ] All images have `alt` text
- [ ] Color contrast passes WCAG AA
- [ ] Keyboard navigation works
- [ ] Forms have associated labels

---

## 4. AI/ML INTEGRATION RULES

**Only integrate AI where it genuinely improves the outcome.**

### When AI IS appropriate:
- Pattern recognition in data that humans cannot manually scan
- Natural language understanding or generation
- Personalization at scale
- Anomaly detection
- Predictive modeling with sufficient data

### When AI is NOT appropriate (use simple logic instead):
- Filtering / sorting (use SQL ORDER BY, not ML)
- Rules-based decisions with < 5 conditions
- Calculations (use math, not neural nets)
- CRUD operations

### LLM Integration Checklist:
- [ ] Prompt injection defense active (load `03-development/prompt-injection-defense`)
- [ ] User inputs wrapped in structural delimiters (not raw string interpolation)
- [ ] LLM responses validated before trusting them
- [ ] Fallback logic if LLM is unavailable
- [ ] Cost controls (token limits, rate limits)
- [ ] No sensitive data sent to external LLM APIs without consent

---

## 5. DATA ARCHITECTURE PRINCIPLES

```
Raw Data
  │
  ▼
Validation Layer (sanitize, type-check, reject bad data)
  │
  ▼
Business Logic Layer (rules, transformations, calculations)
  │
  ▼
Persistence Layer (database, cache, file storage)
  │
  ▼
API Layer (controlled exposure of data to clients)
  │
  ▼
Presentation Layer (UI, mobile, third-party consumers)
```

**Data sovereignty rules:**
- Know where every piece of user data lives
- Apply encryption at rest for sensitive fields (PII, financial)
- Apply TLS for all data in transit
- Define data retention policy (how long do you keep logs / user data?)

---

## 6. TOKEN EFFICIENCY IN EVERY SESSION

These rules save context window and reduce cost:

1. **Skeleton first** — read file structure before reading contents
2. **Symbol extraction** — pull only the function you need to edit
3. **Diff-based review** — review diffs, not full files
4. **Reference, don't paste** — "see `src/api/users.ts` line 45" not the full file
5. **Batch similar tasks** — group all DB schema changes in one step
6. **Checkpoint summaries** — after every 10 actions, write a one-paragraph state summary
7. **Prune dead context** — if a topic is resolved, don't carry it forward

---

## 7. WHEN TO ESCALATE TO THE FULL MASTER BLUEPRINT

Load `references/universal-master-blueprint.md` when the project requires:

- National / government scale audience
- Multi-stakeholder architecture
- AI safety and alignment considerations
- RAG / vector database architecture
- Competitive hackathon judging context
- Business model and unit economics design
- Offline-first or edge deployment
- Multi-lingual / accessibility-first requirements
- Formal presentation to judges, investors, or government bodies
- Full observability and monitoring stack
- Advanced security (threat modeling, penetration testing checklist)

---

## 8. FINAL PROJECT CHECKLIST (Before Shipping)

- [ ] Problem statement fully addressed (not just technically, but meaningfully)
- [ ] All quality gates passed (Section 3)
- [ ] Security checklist complete (Section 3)
- [ ] Live demo works end-to-end without crashes
- [ ] README complete (run `readme-generator` skill)
- [ ] Git history is clean with conventional commit messages
- [ ] Environment variables documented in `.env.example`
- [ ] No TODOs or FIXMEs in production code
- [ ] Performance tested under realistic load
- [ ] Mobile responsive (if web-based)
