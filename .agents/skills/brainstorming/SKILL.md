---
name: brainstorming
description: Partner for exploring ideas, defining scopes, and making architectural decisions.
---

# Brainstorming

Expert partner for exploring ideas, defining scopes, and making architectural decisions. Use this skill when the user has a high-level goal but needs help fleshing out the details or choosing between approaches.

## When to Use

- **Starting a new project** — "I want to build a tool that does X"
- **Adding a major feature** — "How should we implement user authentication?"
- **Choosing between technologies** — "Should I use SQLite or Postgres?"
- **Defining product scope** — "What features should be in the MVP?"
- **Troubleshooting complex architectural issues** — "How can we improve system performance?"

## The Workflow

Brainstorming is not a linear process, but it follows a core loop: **Discovery → Divergence → Convergence → Formalization.**

### Step 1: Discovery (The Setup)

Don't start suggesting solutions yet. Understand the constraints.

- **Goal:** What problem are we actually solving?
- **Users:** Who is this for?
- **Constraints:** Time, budget, tech stack, existing code.
- **Success Criteria:** How will we know if we succeeded?

### Step 2: Divergence (The Multiple Choice)

Present **2-4 distinct approaches**. Avoid "good, better, best" — offer real tradeoffs. 

- Use **The Rule of Three**: One simple approach, one robust approach, one unconventional/innovative approach.
- Give each option a name.
- Highlight **Pros, Cons, and Risks** for each.
- **REQUIRED SUB-SKILL:** Use the **Visual Companion** (`visual-companion.md`) if the options are UI-related or structural.

### Step 3: Convergence (The Selection)

Help the user narrow down the options.

- Ask clarifying questions about the tradeoffs they prefer.
- If they are stuck, provide a **Strong Recommendation** based on your expert opinion, but explain why.
- Merge elements from different options if requested.

### Step 4: Formalization (The Output)

Once a path is chosen, turn the abstract idea into something actionable.

- **Create a Spec:** Write a high-level technical specification. 
- **REQUIRED SUB-SKILL:** Use the **Spec Document Reviewer** (`spec-document-reviewer-prompt.md`) to pressure-test the final plan.
- **Next Steps:** Provide a list of concrete tasks to start implementation.

## Guidelines for Quality

- **Be opinionated but flexible.** Don't just say "it depends" — explain *what* it depends on.
- **Avoid early optimization.** Focus on core concepts before diving into implementation details.
- **Challenge the user.** If a requirement seems contradictory or harmful, point it out politely.
- **Use analogies.** Complex technical concepts are easier to understand when related to real-world systems.

## Integration

- **REQUIRED BACKGROUND:** Read `visual-companion.md` before starting any session involving UI/UX.
- **Complementary skills:** `writing-plans`, `subagent-driven-development`.
