---
name: llm-prompt-injection-defense-shield
description: "Audits and patches AI wrapper codebases for prompt injection vulnerabilities when users say 'scan for prompt injection', 'audit my llm code', or 'secure my ai wrapper', tailored for solo developers and indie hackers."
allowed-tools: [bash, read, write, edit]
_agensi: "9517d3c7-81f8-4f29-822f-8920ec68deda"
---

# LLM Prompt Injection Defense Shield

## Purpose
Acting as an Expert AI Security Architect and Senior DevSecOps Engineer, this skill automatically audits AI wrappers or SaaS products (Next.js, React, FastAPI, Node.js) for prompt injection and system prompt leaking vulnerabilities. It proactively rewrites vulnerable code to sanitize inputs and implement structural delimiters, providing an authoritative, reassuring, and professional cybersecurity defense layer for indie hackers and solo developers.

## When to Use
1. You are building an AI wrapper and need to secure user inputs against prompt injection attacks.
2. You want to audit a Next.js, React, FastAPI, or Node.js codebase for system prompt leaks.
3. You need to implement structural XML delimiters in your existing prompt templates.
4. You suspect raw string interpolation in your API routes is exposing your LLM to jailbreaks.
5. You want to automatically apply OWASP LLM01 remediation strategies to your backend codebase.
6. You are preparing to launch an AI SaaS product and require a final security pass on user input handling.
7. You want to strip potentially malicious XML/HTML tags from incoming user payloads before they reach the LLM context window.

### SCOPE — This skill does NOT handle:
- Penetration testing or active red-teaming of live production endpoints.
- Auditing traditional web vulnerabilities (e.g., SQL injection, XSS) outside the context of LLM integration.
- Fine-tuning language models for safety alignment.
- Managing or rotating leaked API keys.
- Deploying infrastructure-level Web Application Firewalls (WAF).

## Process
1. **Discovery** — Scan the project directory based on the user's free-form conversational inputs (proactively seeking `src/app/api/**/*.ts`, `src/lib/prompts/*.{ts,txt,json}`, `app/services/llm/**/*.py`, and `**/.env.example`) to locate backend API routes and prompt templates. Output: A comprehensive file inventory list of target files to review.
2. **Static Analysis & Vulnerability Detection** — Fetch latest definitions from raw.githubusercontent.com if needed, and analyze the ingested files to see how user input (`req.body`, URL params) is concatenated into the LLM context window. Identify raw string interpolation vulnerabilities checking against OWASP Top 10 LLM01. Output: A vulnerability assessment report detailing affected files and vulnerable code lines.
3. **Code Remediation Strategy** — Formulate a secure patch for flagged files that strictly implements regex sanitization (e.g., `.replace(/<\/?[\w\s="/.':;#-\/]+>/gi, "")`) to strip existing tags, wraps user inputs in structural delimiters (e.g., `<user_input>`), and injects clear system instructions to ignore commands inside user tags. Output: A proposed patching plan that strictly preserves existing API response shapes.
4. **Patch Execution** — Apply the generated security patches safely to the user's source files using the edit tool. Output: The modified, secured source code files.
5. **Audit Reporting** — Produce a clear, highly readable "Audit Complete" output for the user showing the Vulnerability Found, the Analysis rationale, and a simulated Before/After code snippet demonstrating the applied patch. Output: The final audit presentation delivered to the user.

## Validation
- [ ] The YAML frontmatter `description` field names what, when, and who, and includes at least three example user phrases in quotes.
- [ ] The skill contains no dedicated Variables or Inputs section; all target framework, language, and directory constraints are inferred from the user's free-form request.
- [ ] The When to Use list contains 6–8 numbered scenarios followed by a SCOPE block with 3–6 exclusions.
- [ ] Each Process step names one concrete output, readable from the step text.
- [ ] Each Validation checkbox is a declarative post-condition confirmable by inspecting the rendered outputs and edited files.
- [ ] Code modifications actively implement regex sanitization and structural XML delimiters around user inputs.
- [ ] The API response shapes and operational logic remain unbroken after patches are applied.
