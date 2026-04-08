---
name: logic-deep-learning
description: 'Performs exhaustive analysis of a directory to extract functional logic, architectural patterns, and reusable code blocks. Ideal for "copy-and-adapt" scenarios where existing complex logic must be mapped to new project requirements.'
---

# Logic Deep Learning Skill 🧬🧠

This skill is designed to perform a "Deep Learning" audit of existing tools and modules. It focuses on **functional extraction** rather than just architectural description.

## Workflow

### 1. Discovery (Broad Scan)
- List all files and identify the entry points (`main.py`, `app.py`, `index.ts`).
- Identify the "Engine" versus the "Boilerplate".

### 2. Logic Mapping (Deep Dive)
- For every core file, identify:
  - **Inputs/Outputs**: What data structures are passed?
  - **Core Algorithm**: The "magic" part of the code.
  - **Dependencies**: Internal and external libraries used.

### 3. Extraction for Adaptation
- Create a report containing:
  - **Pattern Summary**: The name of the logic pattern (e.g., Router-Dispatch, Chain-of-Thought).
  - **Adaptation Snippets**: Cleaned-up code blocks ready for the NEW architecture.
  - **Gotchas**: Lessons learned or edge cases already handled in the code.

## Execution Prompt

"Analyze the directory [DIR_PATH] and generate a 'DEEP_LEARNING_REPORT.md'. 
Focus on extracting the logic for [USER_OBJECTIVE]. 
Avoid describing general structure; prioritize the 'How it works' and provide snippets that can be adapted to a [TARGET_TECH_STACK] environment."

---
"Study once, reuse forever."
