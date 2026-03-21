---
name: project-bootstrapper
description: Automates the setup of new projects following the SaaS Factory methodology. It initializes the .agents/ folder, installs the Survival Kit, and creates memory files.
---

# Project Bootstrapper 🚀

Expert in project initialization and architecture setup. This skill ensures every project starts with the correct structure, security governance, and intelligence tools.

## The SaaS Factory Trilogy: Template, Lock, and Bootstrap 🚀

This skill implements the **SaaS Factory** methodology, ensuring productivity through project **Hermeticity**.

### 1. Structure & Base Template
Initialize the project following the "Base Template" pattern:
- `.agents/skills/`: Copies the **Survival Kit** (see below) to the local repo. These **MUST** be committed to Git.
- `.agents/rules/`: Global governance rules (Architect, Builder, PM).
- `docs/`: Dedicated documentation folder.

### 2. Survival Kit Injection
Copies these essential skills to the local `.agents/skills/` folder:
- **`Coder`**: High-performance implementation and bug fixing.
- **`Brainstorming` (alias: `writing-plans`)**: Decision-making and scope definition.
- **`Skill-Auditor`**: Security gatekeeper.
- **`Skill-Creator`**: For evolving the project's intelligence.
- **`doc-coauthoring` (alias: `documentation-expert`)**: Professional technical docs.
- **`design-patterns` (alias: `architecture-blueprint-generator`)**: Infrastructure design.
- **`data-governance`**: Naming laws (SSOT).
- **`quality-assurance`**: PDCA stabilization.

### 3. Memory Files (The 3 Scenarios)
Initialize `PLAN.md` with exactly these three execution paths:
- **`O Mais Rápido`**: MVP-focused, minimizing time-to-market.
- **`O Mais Seguro`**: Security-first (OWASP), thorough validation.
- **`O Mais Escalável`**: Architecture-first, microservices, and readiness for high load.

Also initialize `TASKS.md` and high-level project rules (`.windsurfrules`).

### 4. Lock & Env
- **`skills-lock.json`**: Creates a lock file mapping the exact versions of the injected skills.
- **`.env.example`**: Standardized environment variables.

---

## Guidelines
- **Hermeticity**: Tell the user that all skills in `.agents/skills` **should be committed to Git**.
- **Context-Awareness**: Before finalizing, ask for the **Main Goal** and **Tech Stack**.
- **Absolute Paths**: Ensure all file operations use absolute paths to avoid context loss.
