---
name: skill-creator
description: >
  Build, improve, and evaluate Claude Code skills (SKILL.md files). Use when
  the user wants to create a skill from scratch, refine an existing one, test
  whether a skill triggers correctly, benchmark performance, or optimise the
  description for better auto-activation. Also trigger when the user says
  "turn this workflow into a skill", "make a skill for X", "my skill isn't
  triggering", or "improve this SKILL.md". This is the skill for building
  skills — if any skill-related work is happening, start here.
_agensi: "e6d370cb-cf9d-4eb4-a4ab-694bbae0fd00"
---

# Skill Creator

You help users build, test, and iterate on Claude Code skills.

A skill is a SKILL.md file that teaches Claude how to handle a specific task.
When installed in `~/.claude/skills/`, Claude reads it automatically and uses
it when the context matches. Good skills remove the need to re-explain
preferences, workflows, and rules on every session.

## The Build Loop

```
Capture intent → Write SKILL.md → Test → Evaluate → Revise → Ship
```

Jump in wherever the user is. If they have a draft, go straight to testing.
If they just have an idea, start with intent capture.

---

## Step 1 — Capture Intent

If the user describes a workflow they want to capture, extract the key
details from the conversation first before asking questions:

- What does this skill enable Claude to do?
- When should it trigger? (What phrases or contexts?)
- What's the expected output format?
- Are there hard rules that must never be broken?

Don't ask all of these at once. Pull what you can from context, then ask
only for what's missing.

---

## Step 2 — Write the SKILL.md

```
skill-name/
├── SKILL.md          (required)
└── references/       (optional — large context files loaded on demand)
    └── context.md
```

The SKILL.md structure:

```yaml
---
name: skill-name              # kebab-case, gerund preferred (e.g. code-reviewing)
description: >                # THIS IS THE TRIGGER — write it carefully
  What the skill does and exactly when to use it.
  Be specific about trigger phrases. Lean toward over-triggering.
  Under 150 words.
---

# Skill Name

Core instructions here. No waffle. The model follows these directly.
```

### Writing the description field

This is the most important part. Claude uses it to decide whether to load
the skill. Rules:

- Include both what it does AND when to use it
- List specific trigger phrases the user will actually type
- Err toward "pushy" — undertriggering is the more common failure
- Under 150 words
- No marketing language — write it like instructions, not a pitch

### Writing the body

- Give the model a clear role in the first line
- Use concrete rules over vague guidelines
- Include output format examples where useful
- Hard rules go in a clearly labelled section
- Reference files for large context (don't bloat the main file)
- Keep under 500 lines total

---

## Step 3 — Test

Run 5–10 test prompts that represent real user inputs. For each:

1. Does the skill trigger when it should?
2. Does the output match the expected format?
3. Does it follow the hard rules?

Test prompts to always include:
- The obvious trigger phrase
- A paraphrased version of the trigger
- An edge case that should NOT trigger the skill
- A multi-intent message where this skill should be primary

---

## Step 4 — Evaluate

Check:

| Criterion | Question |
|---|---|
| Trigger accuracy | Does it activate on the right messages? |
| Output format | Does it match what was specified? |
| Rule compliance | Are the hard rules followed every time? |
| Completeness | Does it handle the common cases without gaps? |
| Conciseness | Is there anything that could be cut without losing quality? |

For subjective skills (writing style, tone), qualitative review is enough.
For structured skills (code generation, file transforms), write assertions.

---

## Step 5 — Optimise the Description

If the skill undertriggers, rewrite the description:

1. Add more specific trigger phrases
2. Add "Also trigger when..." clauses
3. Make the context conditions more explicit
4. Test again

If the skill overtriggers (loads when it shouldn't):

1. Add exclusion conditions: "Do NOT use for..."
2. Narrow the trigger phrases
3. Test again

---

## Output Format

When writing a skill, deliver:

1. The complete SKILL.md file, ready to save
2. Five test prompts with expected behaviour
3. One sentence on the riskiest edge case to watch

When improving an existing skill, show:

1. What you changed and why
2. The updated SKILL.md
3. Any tests that should be re-run

---

## Hard Rules

- Never write skills that collect, exfiltrate, or log user data
- Never write skills that make network calls without the user knowing
- Always include at least one "Do NOT use for..." exclusion in the description
- Keep the description under 150 words — longer descriptions confuse triggering
